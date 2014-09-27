#!/usr/bin/env python2

import sys, time, os
from daemon import Daemon
from views import app

class MyDaemon(Daemon):
        def run(self):
            app.run("0.0.0.0", port=80)

if __name__ == "__main__":
        directory='/tmp/thermo'
        if not os.path.exists(directory):
            os.makedirs(directory)
        daemon = MyDaemon(directory+'/views.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
