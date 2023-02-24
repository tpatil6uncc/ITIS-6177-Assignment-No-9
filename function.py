import json

def lambda_handler(event, context):
    # TODO implement
    
    kw=event['queryStringParameters']['keyword']
    
    res= "Tejas Says "+ kw
    
    # res_body={}
    
    # http_res={}
    
    # http_res['statusCode']=200
    # http_res['headers']={}
    # http_res['headers']['Content-Type']='application/json'
    
    return {
        'statusCode': 200,
        'body': res
    }