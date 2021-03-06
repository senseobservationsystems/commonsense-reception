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


from wsgiref.simple_server import make_server
import threading
import logging_sense

class Reception():

    def __init__(self, port):
        self.logger = logging_sense.Logger()
        self.__port = port
        
        try:
            self.initialize()
        except:
            pass
        
        self.__server = make_server('localhost', self.__port, self.__handle_request__)
        self.__server.serve_forever()
            
    def __handle_request__(self, environ, start_response):
        # preferably here some anti-spam mechanism... need to check if this is a reasonable request
        response_status     = '500 Internal Server Error'
        response_body       = ''
        response_headers    = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
        
        url     = environ.get('PATH_INFO', '/')
        method  = environ.get('REQUEST_METHOD', 'GET')
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except:
            request_body_size = 0
        
        if request_body_size > 0:
            request_body = environ['wsgi.input'].read(request_body_size)
        else:
            request_body = ''
        
        if url == '/register':
            if method == 'POST':
                try:
                    p = threading.Thread(target=self.handle_register, args=[request_body])
                    p.start()
                except:
                    pass
                response_status, response_headers, response_body = self.register_response(request_body)
            else:
                response_status     = '405 Method Not Allowed'
                response_body       = ''
                response_headers    = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
                
        elif url == '/in':
            if method == 'POST':
                try:
                    p = threading.Thread(target=self.handle_in, args=[request_body])
                    p.start()
                except:
                    pass
                response_status, response_headers, response_body = self.in_response(request_body)
            else:
                response_status     = '405 Method Not Allowed'
                response_body       = ''
                response_headers    = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]           
                 
        elif url == '/out':
            if method == 'GET':
                try:
                    p = threading.Thread(target=self.handle_out, args=[request_body])
                    p.start()
                except:
                    pass
                response_status, response_headers, response_body = self.out_response(request_body)
            else:
                response_status     = '405 Method Not Allowed'
                response_body       = ''
                response_headers    = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]         
                   
        else:
            response_status, response_headers, response_body = self.__not_found__()
                
        start_response(response_status, response_headers)
        return [response_body] 

    def __not_found__(self):
        # set response parameters
        status              = '404 Not Found'
        response_body       = ''
        response_headers    = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
        
        # return the response
        return status, response_headers, response_body
        
        
    def register_response(self, request_body):
        # set response parameters
        status              = '200 OK'
        response_body       = '<html><body>Thank you!</body></html>'
        response_headers    = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
        
        # return the response
        return status, response_headers, response_body

    def in_response(self, request_body):
        # set response parameters
        status              = '200 OK'
        response_body       = '<html><body>Thank you!</body></html>'
        response_headers    = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
        
        # return the response
        return status, response_headers, response_body

    def out_response(self, request_body):
        # set response parameters
        status              = '200 OK'
        response_body       = '<html><body>Thank you!</body></html>'
        response_headers    = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
        
        # return the response
        return status, response_headers, response_body
        
