import os
import rospkg
import rospy

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget, QShortcut
from python_qt_binding.QtCore import Qt, QTimer, Slot
from python_qt_binding.QtGui import QKeySequence
from std_msgs.msg import Int64, String, Int32

class MyPlugin(Plugin):

    def __init__(self, context):
        super(MyPlugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('MyPlugin')
        rp = rospkg.RosPack()

        # Process standalone plugin command-line arguments
        from argparse import ArgumentParser
        parser = ArgumentParser()
        # Add argument(s) to the parser.
        parser.add_argument("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print 'arguments: ', args
            print 'unknowns: ', unknowns

        # Create QWidget
        self._widget = QWidget()
        # Get path to UI file which is a sibling of this file
        # in this example the .ui and .py file are in the same folder
        ui_file = os.path.join(rp.get_path('rqt_mypkg'), 'resource', 'MyPlugin.ui')
        # Extend the widget with all attributes and children from UI file
        loadUi(ui_file, self._widget)
        # Give QObjects reasonable names
        self._widget.setObjectName('MyPluginUi')
        # Show _widget.windowTitle on left-top of each plugin (when 
        # it's set in _widget). This is useful when you open multiple 
        # plugins at once. Also if you open multiple instances of your 
        # plugin at once, these lines add number to make it easy to 
        # tell from pane to pane.
        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        # Add widget to the user interface
        context.add_widget(self._widget)
        self._widget.go1.pressed.connect(self._on_go1_pressed)
        self._widget.go2.pressed.connect(self._on_go2_pressed)
        self._widget.go3.pressed.connect(self._on_go3_pressed)
        self._widget.go4.pressed.connect(self._on_go4_pressed)
        self._widget.go5.pressed.connect(self._on_go5_pressed)
        self._widget.go6.pressed.connect(self._on_go6_pressed)
        self._widget.go7.pressed.connect(self._on_go7_pressed)
        self._widget.go8.pressed.connect(self._on_go8_pressed)
        self._widget.go9.pressed.connect(self._on_go9_pressed)
        self._widget.go10.pressed.connect(self._on_go10_pressed)

    @Slot(str)
    def _on_go1_pressed(self):
        global go1
        go1 = int(1)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go1)


    def _on_go2_pressed(self):
        global go2
        go2 = int(2)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go2)


    def _on_go3_pressed(self):
        global go3
        go3 = int(3)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go3)


    def _on_go1_pressed(self):
        global go1
        go1 = int(1)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go1)


    def _on_go4_pressed(self):
        global go4
        go4 = int(4)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go4)


    def _on_go5_pressed(self):
        global go5
        go5 = int(5)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go5)


    def _on_go6_pressed(self):
        global go6
        go6 = int(6)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go6)


    def _on_go7_pressed(self):
        global go1
        go7 = int(7)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go7)


    def _on_go8_pressed(self):
        global go8
        go8 = int(8)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go8)


    def _on_go9_pressed(self):
        global go9
        go9 = int(9)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go9)


    def _on_go10_pressed(self):
        global go10
        go10 = int(10)
        try:
            self._publisher = rospy.Publisher("options", Int64, queue_size=1000)
        except TypeError:
            self._publisher = rospy.Publisher("options", Int64)
        self._publisher.publish(go10)

    def shutdown_plugin(self):
        # TODO unregister all publishers here
        pass

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    #def trigger_configuration(self):
        # Comment in to signal that the plugin has a way to configure
        # This will enable a setting button (gear icon) in each dock widget title bar
        # Usually used to open a modal configuration dialog
