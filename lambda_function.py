import tensorflow as tf
import sys
def handler(event, context):
    
    print(tf.__version__)

    return {
        "message": 'Hello from AWS Lambda using Python' +'(sys: ' + sys.version + '), (tf: ' + tf.__version__ + ')' + '!',
        }