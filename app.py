from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()


#import time
#import redis

#from flask import Flask
#app = Flask(__name__)

#cache = redis.Redis(host='localhost', port=6379)

#def my_function():
#    retries = 5
#    while True:
#        try:
#            return cache.incr('hits')
#        except redis.exceptions.ConnectionError as exc:
#            if retries == 0:
#                raise exc
#            retries -= 1
#            time.sleep(0.5)

#def hello():
#    count = my_function()
#    return 'Hello world! I have been seen () times.\n'.format(count)

#if app == "__main__":
#    app.run(host="0.0.0.0",debug=True)
