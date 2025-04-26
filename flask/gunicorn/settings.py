#
# Gunicorn config file
#
wsgi_app = 'app:app'

# Server Mechanics
#========================================
# current directory
chdir = '/app'

# daemon mode
daemon = False

# enviroment variables
raw_env = [

]

# Server Socket
#========================================
bind = '0.0.0.0:5000'

# Worker Processes
#========================================
workers = 2

#  Logging
#========================================
# access log
accesslog = '/var/log/gunicorn/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# gunicorn log
errorlog = '/var/log/gunicorn/error.log'
loglevel = 'info'