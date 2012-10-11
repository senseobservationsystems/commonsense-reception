""" 
Copyright (C) [2012] Sense Observation Systems B.V.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 
http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import datetime



class Logger ():
    
    def __init__ (self):
        self.debug_logging = False
        self.error_logging = True
        self.error_file = '../logs/error_log.sos.txt'

    def setErrorLoggingOn (self):
        self.error_logging = True
        
    def setErrorLoggingOff (self):
        self.error_logging = False
        
    def setErrorPrefix (self, s):
        self.error_prefix = s
        
    def setErrorFile (self, f):
        self.error_file = f
        
    def error (self, string): 
        if self.error_logging == True:
            try:
                f = open(self.error_file, 'a')
                f.write('{0} - {1} - {2}\n'.format(datetime.datetime.now(), self.error_prefix, string))
                f.close()
            except:
                pass

        
    def setDebugLoggingOn (self):
        self.debug_logging = True
        
    def setDebugLoggingOff (self):
        self.debug_logging = False 
    
    def debug (self, string):
        if self.debug_logging == True:
            print string
           
