__doc__="""
$Revision: 0.0 $

Will dynamically launch molecular dynamics simulations on GPU's and allow
the user to visualize the simulation in real time.

Author: Levi Pierce levipierce@gmail.com 
"""
import sys, os, re
import threading, time
from subprocess import Popen, PIPE
from PyQt4.QtGui import QDialog, QApplication, QPixmap
from PyQt4.QtCore import Qt
from nvidia_expo_gui_dir.nvidia_expo_gui_ui import Ui_Dialog 
import vmd.control as vmd_controller

#GLOBALS MUST BE SET
CWD = os.getcwd()
VMD_DIR = os.path.join(CWD, 'vmd')
VMD_RUN = ['vmd','-e','remote_ctl.tcl'] 
NVIDIA_IMAGE = os.path.join(CWD,'images_nvidia.jpg')
AMBER_IMAGE = os.path.join(CWD,'images_amber.jpg')
AMBERHOME = os.environ['AMBERHOME']
PMEMDCUDA = os.path.join(AMBERHOME,'bin','pmemd.cuda')
SIMDIR = os.path.join(CWD,"JAC_production_NVE")
MDIN = os.path.join(SIMDIR, 'mdin')
MDINFO = os.path.join(SIMDIR,'mdinfo')
PRMTOP = os.path.join(SIMDIR, 'dhfr.parm')
NETCDF = os.path.join(SIMDIR, 'mdout.nc')
# Interval in seconds to wait before attempting to read mdinfo again
READ_MDINFO_INTERVAL = 2
# Interval in seconds to wait before attempting to read trajectory again
READ_TITAN_TRAJ_INTERVAL = 0.25
READ_640_TRAJ_INTERVAL = 1.50
# Set how you want everything to be displayed then save it
VMD_STATE=os.path.join(SIMDIR,'visualize_dhfr.vmd')


# CUDA VISIBLE DEVICE MAP
GFX_MAP = {'titan' : '0', '640' : '1'}

def findIt(w):
    """
    """ 
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def get_cmd():
    """
    """
    cmd = [PMEMDCUDA, '-O','-x', NETCDF, '-p', PRMTOP]

    return cmd

class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        # instance of vmd server
        self.vmd_server = None
        # timer
        self.timer = None
        # trajectory read timer
        self.traj_timer = None
        # instance of amber simulation
        self.sim = None
        # Set up user interface from designer
        self.setupUi(self)
        # Connect up the buttons.
        self.gtx_640_run_button.clicked.connect(self.gtx_640_run)
        self.gtx_titan_run_button.clicked.connect(self.gtx_titan_run)

        self.nvidia_image_label.setGeometry(10,10,400,100)
        self.nvidia_image_label.setPixmap(QPixmap(NVIDIA_IMAGE))

        self.amber_image_label.setGeometry(10,10,400,100)
        self.amber_image_label.setPixmap(QPixmap(AMBER_IMAGE))

        self.launch_vmd()

    def gtx_640_run(self):
        """
        """
        self.init_sim()
        if self.traj_timer:
            self.traj_timer.stop()
        os.environ['CUDA_VISIBLE_DEVICES'] = GFX_MAP['640']
        self.sim = Popen(get_cmd())
        self.timer = RepeatEvery(READ_MDINFO_INTERVAL, 
                  self.read_mdinfo, self.gtx_640_lcdNumber)
        self.timer.start()
        self.traj_timer = RepeatEvery(READ_640_TRAJ_INTERVAL, 
                  self.read_trajectory)
        self.traj_timer.start()

    def gtx_titan_run(self):
        """
        """
        self.init_sim()
        if self.traj_timer:
            self.traj_timer.stop()
        os.environ['CUDA_VISIBLE_DEVICES'] = GFX_MAP['titan']
        self.sim = Popen(get_cmd())
        self.timer = RepeatEvery(READ_MDINFO_INTERVAL, 
                  self.read_mdinfo, self.gtx_titan_lcdNumber)
        self.timer.start()
        self.traj_timer = RepeatEvery(READ_TITAN_TRAJ_INTERVAL, 
                  self.read_trajectory)
        self.traj_timer.start()
 
    def init_sim(self):
        """
        """
        if self.sim:
            self.sim.kill()
        if self.timer:
            self.timer.stop()
        if os.path.isfile(MDINFO):
            os.remove(MDINFO)
        os.chdir(SIMDIR)
    
    def read_trajectory(self):
        """
        This call gets made every READ_TRAJ_INTERVAL seconds.
        Currently set to 5 so in 5 seconds we should read 125 frames.
        """
        # How fast can vmd read frames...system dependent
        start_delay = 10
        count = self.traj_timer.counter - start_delay
        print count
        beg = count 
        end = (count) 
        if count > -1:
            cmd = "animate read netcdf %s beg %d end %d"%(NETCDF, beg, end)
            self.vmd_server.command(cmd)
        
    def read_mdinfo(self, lcdNumber):
        """
        """
        try:
            fh = open(MDINFO, 'r')
        except IOError:
            # Handle this somehow...
            return
        else:
            for line in fh:
                if findIt('ns/day')(line):
                    lcdNumber.display(float(line.split()[3]))
                    fh.close()
                    return

    def launch_vmd(self):
        """
        """
        self.vmd_server = vmd_controller.server()
        self.vmd_server.command('play %s'%VMD_STATE)

    def keyPressEvent(self, event):
        """
        """
        if event.key() == Qt.Key_P:
            print "paused"
            if self.timer:
                self.timer.pause()
            if self.traj_timer:
                self.traj_timer.pause()
        if event.key() == Qt.Key_R:
            print "running"
            if self.timer:
                self.timer.resume()
            if self.traj_timer:
                self.traj_timer.resume()
                print "-->", self.traj_timer.runable
       
    def closeEvent(self, event):
        """
        """
        if self.timer:
            self.timer.stop()
        if self.traj_timer:
            self.traj_timer.stop()
        if self.sim:
            self.sim.kill()
        if self.vmd_server:
            self.vmd_server.stop()

class RepeatEvery(threading.Thread):
    def __init__(self, interval, func, *args, **kwargs):
        """
        """
        threading.Thread.__init__(self)
        self.counter = 0
        self.paused = False
        self.interval = interval
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.runable = True

    def run(self):
        """
        """
        while self.runable:
            if not self.paused:
                self.func(*self.args, **self.kwargs)
                self.counter += 1
            time.sleep(self.interval)

    def pause(self):
        """
        """
        self.paused = True

    def resume(self):
        """
        """
        self.paused = False

    def stop(self):
        """
        """
        self.runable = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    nvidia_app = Dialog()
    nvidia_app.show()
    sys.exit(app.exec_())

