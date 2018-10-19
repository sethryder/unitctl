import getopt
import json
import sys

import requests
import requests_unixsocket

unit_socket = '/var/run/control.unit.sock'

class UnitCtl:
    def __init__:
        return True
    
    def get_config(application):
        return True

    def load_config(application, config):
        return True

    def remove_config(application):
        return True
    
    def reload_application(application):
        return True

class UnitRequest:
    def __init__(socket):
        self.socket = socket
        self.session = requests_unixsocket.Session()

    def send_get_request(path, payload):
        result = self.session.get(self.socket + path)
        return result

    def send_put_request(path, payload):
        result = self.session.put(self.socket + path)
        return result


class UnitHelper:
    def validate_json(json):
        return True
    
    @staticmethod
    def usage():
        print 'Usage: unitctl.py (option)'
        print ''
        print '-g, --get-config [<application>]         Get the entire config or the config for one application.'
        print '-l, --load-config <application>          Load a config. If the applicaiton exists it will overwrite it.'
        print '-d, --remove-config <application>        Remove the application/config.'
        print '-r, --reload_application <application>   Reload an application.'
        print ''

def main:
    try:
        opts, args = getopt.getopt(sys.argv[1:], "gldrh", [
          "get-config",
          "load-config",
          "remove-config",
          "reload-application",
          "help"])
    except getopt.GetoptError, err:
        print str(err) # will print something like "option -z not recognized"
        UnitHelper.usage()
        sys.exit(2)
    for opt, arg in opts:
        ran = True
        if opt in ("-g", "--get-config"):
            return True
        elif opt in ("-l", "--load-config"):
            return True
        elif opt in ("-d", "--remove-config"):
            return True
        elif opt in ("-r", "--reload-application"):
            return True
        elif opt in ("-h", "--help"):
            UnitHelper.usage()
        else:
           assert False, "unhandled option"

    if not ran:
        usage()

if __name__ == "__main__":
    main()

#r = session.get('http+unix://%2Ftmp%2Fprofilesvc.sock/path/to/page')
#assert r.status_code == 200
