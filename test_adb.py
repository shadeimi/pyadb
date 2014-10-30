__author__ = 'cpp'

from pyadb import ADB
import unittest
from unittest import TestCase
import sys

class TestAdbLibrary(TestCase):
    __adb = None
    __adbpath = ""
    
    def setUp(self):
#         for arg in sys.argv:
#             print arg
#         if len(sys.argv) == 1 or  not sys.argv[1]:
#             print "invalid adb path"
#             sys.exit(1)
#       print "Execute with adb path " + sys.argv[1]
#       self.__adb = ADB(sys.argv[1])
        self.__adbpath = "/Users/pier/bin/android-sdk-macosx/platform-tools/adb"
        self.__adb = ADB(self.__adbpath) 
    
    def tearDown(self):
        print "tearDown"
        self.__adb.kill_server()
        
    def _getSerial(self):
        self.__adb.start_server()
        devices = self.__adb.get_devices()
        print "------------------------------------------------------"
        print devices
        print "------------------------------------------------------"
        serial = devices[1][0]
        self.__adb.kill_server()
        return serial
      
    def test_with_nothing(self):
        print "test_with_nothing"
        cmd =  " ".join(self.__adb.get_run_cmd('devices'))
        cmd_aspected = self.__adbpath + " " + "devices"
        self.assertEqual(cmd,cmd_aspected)
         
    def test_with_host(self):
        print "test_with_host"
        self.__adb.set_host("127.0.0.1")
        cmd =  " ".join(self.__adb.get_run_cmd('devices'))
        cmd_aspected = self.__adbpath + " -H " + "127.0.0.1" + " " + "devices"
        self.assertEqual(cmd,cmd_aspected)
         
    def test_with_port(self):
        print "test_with_port"
        self.__adb.set_port("4447")
        cmd =  " ".join(self.__adb.get_run_cmd('devices'))
        cmd_aspected = self.__adbpath + " -P " + "4447" + " " + "devices"
        self.assertEqual(cmd,cmd_aspected)
     
    def test_with_serial(self):
        print "test_with_serial"
        serial = self._getSerial()
        self.__adb.set_target_device(serial)
        cmd =  " ".join(self.__adb.get_run_cmd('devices'))
        cmd_aspected = self.__adbpath + " -s " + serial + " " + "devices"
        self.assertEqual(cmd,cmd_aspected)
     
    def test_with_host_port(self):
        print "test_with_host_port"
        self.__adb.set_host("127.0.0.1")
        self.__adb.set_port("4447")
        cmd =  " ".join(self.__adb.get_run_cmd('devices'))
        cmd_aspected = self.__adbpath + " -H " + "127.0.0.1" + " -P " + "4447" + " " + "devices"
        self.assertEqual(cmd,cmd_aspected)
     
    def test_with_host_serial(self):
        print "test_with_host_serial"
        self.__adb.set_host("127.0.0.1")
        serial = self._getSerial()
        self.__adb.set_target_device(serial)
        cmd =  " ".join(self.__adb.get_run_cmd('devices'))
        cmd_aspected = self.__adbpath + " -H " + "127.0.0.1" + " -s " + serial + " " + "devices"
        self.assertEqual(cmd,cmd_aspected)
 
    def test_with_port_serial(self):
        print "test_with_port_serial"
        self.__adb.set_port("4447")
        serial = self._getSerial()
        self.__adb.set_target_device(serial)
        cmd =  " ".join(self.__adb.get_run_cmd('devices'))
        cmd_aspected = self.__adbpath + " -P " + "4447" + " -s " + serial + " " + "devices"
        self.assertEqual(cmd,cmd_aspected)
    
    def test_with_host_port_serial(self):
        print "test_with_host_port_serial"
        self.__adb.set_host("127.0.0.1")
        self.__adb.set_port("4447")
        serial = self._getSerial()
        self.__adb.set_target_device(serial)
        cmd =  " ".join(self.__adb.get_run_cmd('devices'))
        cmd_aspected = self.__adbpath + " -H " + "127.0.0.1" + " -P " + "4447" + " -s " + serial + " " + "devices"
        self.assertEqual(cmd,cmd_aspected)

if __name__ == '__main__':
    unittest.main()

