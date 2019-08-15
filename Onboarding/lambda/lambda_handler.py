import boto3

dynamodb = boto3.resource('dynamodb', region_name = "us-west-1")

def lambda_handler(event, context):
    parsed = event['body'].split('&')
    
    d = {}
    for parameter in parsed:
        parameter = parameter.split('=')
        d[parameter[0]] = parameter[1].replace("+"," ")
        
    table = dynamodb.Table("Onboarding")
    table.put_item(Item = { "QRCode": d['QRCode'], 'name': d['name'], 'exposure_vector': d['exposure_vector']  })

    html = '<!DOCTYPE html><p> Enjoy your experience, ' + str(d['name']) +  '</p>'

    return html