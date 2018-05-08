Python + AWS Lambda + Twilio
===

Using Python, Twilio and AWS Lambda to create a texting app.

##### By: Darye Henry - CTO @ DeveloperTown Starts

---
Guidelines
===
- Create a proof of concept trivia texting app in 30 mins or less
- No servers
- Don't know a lot about Python - hopefully will want to learn more :)

---
Technologies used:
===

- AWS Lambda
- AWS API Gateway
- Python 2.7
- Twilio

---
Getting Started
===
- Does not take a lot of code 
- More Lambda and API Gateway configuration than code for a very simple app

---
Minimal code required
===
```
def lambda_handler(event, context):
    
    return "Thanks for texting"
```
---
Create Lambda Function in AWS
===

# ![](create-function.png)

---
Create your custom role
===
# ![](create-custom-role.png)

---
Add an API Gateway
===
# ![](add-api-gateway-1.png)

---
Add Code
===
```
def lambda_handler(event, context):

    message = unicode(str(event['Body']), 'utf-8')
    phone_number = event['From']

    if message.lower() == u"start":
        return "In California, it is illegal to eat oranges while doing what?\n1) Gardening\n2) Bathing\n3) Driving\n4) Working on a computer";
    elif message == "2" or message.lower() == "bathing":
        return "Lucky guess"
    elif message == "1" or message.lower() == "gardening":
        return "Wrong, you lose"
    elif message == "3" or message.lower() == "driving":
        return "Nope"
    elif message == "4" or message.lower() == "working on a computer":
        return "It is literally impossible for you to be more wrong"
```

---
Add Code
===
1. In your local environment create a new project folder
2. Add a file called `lambda_function.py`
3. Download the Python Twilio Library
4. Zip `lambda_function.py` and the `twilio` folder 
5. Upload .zip file to lambda

---
Add Code
===
# ![](add-code.png)

---
Configure your test event
===
# ![](configure-test-event.png)

---
Configure your test event
===
# ![35%](configure-test-event-2.png)

---
Configure your API
===

---
Create a new "GET" method
===
# ![50%](actions-menu.png)

---
Create a new "GET" method
===
Enter your lamda
# ![](select-your-lamda.png)

---
Get Method Details
===
# ![](api-get-method.png)

---
Integration Request
===
Insert template to transform GET params to JSON
# ![35%](integration-request-3.png)

---
Method Response
===
Change to `application/xml`
# ![](method-response.png)

---
Integration Response
===
Change to `application/xml`, enter in Twilio XML Format as template
# ![](integration-response.png)

---
Almost forgot - Deploy your API !!
===
Save yourself wasted debugging time
# ![](deploy-api.png)

---
Setup Twilio
===
1. Create New Phone Number
2. Go to Manage Numbers > Active Numbers
3. Select your Phone Number
4. Edit Messaging WebHook - Insert your API Url

# ![](messaging-webhook.png)

---
End Results
===
# ![50%](txt-msg-shot.png)
---

You are ready to test!
===
Text **"Start"** to **317-827-7668** (or your Twilio number)


---
Inspiration: Call Me In 5
===

- Quit asking friends to interrupt dates and meetings. 
- Feel important
- Get interrupted by just telling `Call Me In 5` to call you in 5 mins (or whatever)

---
Try it out!
===
Text **"Hey"** to **317-854-0143**

---
Connect
===
- GitHub: github.com/darye
- email: dhenry@developertown.com
- twitter: @darye











