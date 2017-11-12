

import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask_kbritikov.settings")

application = get_wsgi_application()


def simple_app(environ, start_response):
    f = open("/home/chapay/TechPark/Web/ask_kbritikov/templates/Base.html")
    text = f.read()
    data = bytes(text, 'utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

def dapp(environ,start_response):
    info=bytes("Hello World\n",'utf-8')
    if environ.get("REQUEST_METHOD") =='GET' and environ["QUERY_STRING"]:
        print("Method:GET",'\n',environ["QUERY_STRING"]+'\n')
    if environ.get("REQUEST_METHOD") == 'POST' and environ["wsgi.imput"]:
            print("Method:POST", '\n', environ["wsgi.input"].read() + '\n')
    status ='200 OK'
    response_headers=[('Content-type','text/plain')]
    start_response(status, response_headers)
    return iter([info])
# def simple_app(environ, start_response):
#     """Simplest possible application object"""
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/plain')]

#     start_response(status, response_headers)
#     return ['Hello world!\n']
#
#
# def application(environ, start_response):
#     """Simplest possible application object"""
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/plain')]
#     start_response(status, response_headers)
#     return ['Hello world!\n']
# #
# class AppClass:
#     """Produce the same output, but using a class
#
#     (Note: 'AppClass' is the "application" here, so calling it
#     returns an instance of 'AppClass', which is then the iterable
#     return value of the "application callable" as required by
#     the spec.4
#
#     If we wanted to use *instances* of 'AppClass' as application
#     objects instead, we would have to implement a '__call__'
#     method, which would be invoked to execute the application,
#     and we would need to create an instance for use by the
#     server or gateway.
#     """
#
#     def __init__(self, environ, start_response):
#         self.environ = environ
#         self.start = start_response
#
#     def __iter__(self):
#         status = '200 OK'
#         response_headers = [('Content-type', 'text/plain')]
#         self.start(status, response_headers)
#         yield "Hello world!\n"
#
