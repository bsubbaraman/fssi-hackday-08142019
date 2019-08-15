import json
import boto3


def writeToDB(qr):
    table = dynamodb.Table("QRScan")
    table.put_item(Item = { "QRCode": qr, "meta": '{ "room": "1", "content-type": "String" }' })
    response = table.get_item(Key={"QRCode": qr})
    print(response["Item"]["meta"])
    
client = boto3.client('sns')
dynamodb = boto3.resource('dynamodb', region_name = "us-west-1")

while True:
    qr = input("Scan QR Code: \n")  ## note: scanner must be configured with carriage return suffix for automated behaviour 
    print("qr code is " + qr)
    
    message = {"QR Code": qr}#, "room": "2"}
    response = client.publish(
    TargetArn='arn:aws:sns:us-west-1:428861092905:qr-test',
    Message=json.dumps({'default': json.dumps(message)}),
    MessageStructure='json'
    )
    
    writeToDB(qr)



