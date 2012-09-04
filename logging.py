'''
Created on Aug 23, 2012

@author: Freek van Polen
'''

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
           
