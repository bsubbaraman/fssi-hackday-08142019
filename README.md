# Hackday: Aug 14
#fssi2019/hackdays

## QR Scanner to SNS Publisher for Raspberry Pi
* Running `qr_scanner.py` will allow you to scan QR codes
* The QR code is published to an sns topic:
	* topic ARN: `arn:aws:sns:us-west-1:428861092905:qr-test`
	* Tested full loop of receiving topic in TouchDesigner (with Rey)
* Data also written to DynamoDB database with room number
* Currently only allowing database writes from the account on which it was created
* To-do:
	* Run headless with `qr_scanner.py` running on start-up 
* Note: The USB Barcode scanner needs to be configured with a carriage-return suffix, so that upon scanning it ‘enters’ it’s value 



## Onboarder
* Working from [this guide](https://blog.summercat.com/using-aws-lambda-and-api-gateway-as-html-form-endpoint.html)
* Lambda + API Gateway to create an HTTP endpoint that accepts POST requests and write to DynamoDB
* Working Website: http://fssi-onboarding.s3-website-us-west-1.amazonaws.com/
* After hitting _Submit_, the data is written to a dynamoDB table
* To-Do:
	* Offboarding: if same QR code scanned again, remove item from database
	* Error Checking: make sure no fields blank, exposure vector values are reasonable, etc


* AWS Resources/notes
	* [Host a static website using s3](https://aws.amazon.com/getting-started/projects/build-serverless-web-app-lambda-apigateway-s3-dynamodb-cognito/module-1/)
		* Will get a warning about public access, but this is anticipated; we are making the bucket read-only to everybody so that anybody can access the webpage
	* After deploying an API, if any changes are made and saved, it is still required to _re-deploy the API_ for changes to be made
	* 





