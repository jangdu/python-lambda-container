import tensorflow as tf 
import json import io
import sys 

def handler(event, context): 
    old_stdout = sys.stdout 
    new_stdout = io.StringIO() 
    sys.stdout = new_stdout 
    code_text = event['data'] 
    exec(code_text, globals()) 

    sys.stdout = old_stdout
    printed_output = new_stdout.getvalue()

    # ensure_ascii=False를 추가하여 유니코드 문자를 그대로 유지하고, 결과를 UTF-8로 인코딩 
    utf8_output = json.dumps(printed_output, ensure_ascii=False).encode('utf-8') 

    return { 'statusCode': 200, 'data': utf8_output }