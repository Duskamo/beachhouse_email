from flask import Flask, request
import os
from src.EmailClient import EmailClient
from src.Data import Data
app = Flask(__name__)

# Data POST Requests
@app.route('/contact', methods=['POST'])
def send_contact():
	# Gather Data
	contactInfo = request.json
	
	# Send email to dlandry email server using client contact info
	emailClient = EmailClient()

	emailClient.addUserEmail(contactInfo['email'])
	emailClient.addUserName(contactInfo['name'])
	emailClient.addSubject(contactInfo['subject'])
	emailClient.addMessage(contactInfo['message'])

	emailClient.send()

	# Return status code
	return "200"

@app.route('/email_booking_confirmation_to_owner', methods=['POST'])
def email_booking_confirmation_to_owner():
	# Gather Data
	bookingInfo = request.json
	
	# Send email to dlandry email server using client contact info
	emailClient = EmailClient()

	emailClient.addUserEmail(bookingInfo['contactInfo']['email'])
	emailClient.addUserName(bookingInfo['contactInfo']['firstName'] + " " + bookingInfo['contactInfo']['lastName'])
	emailClient.addSubject(Data.bookedSubject)
	emailClient.addMessage(Data.bookedMessage.format(bookingInfo['rentalInfo']['arrivalDate'],bookingInfo['rentalInfo']['departDate']))

	emailClient.send()

	# Return status code
	return "200"

@app.route('/text_booking_confirmation_to_owner', methods=['POST'])
def text_booking_confirmation_to_owner():
	# Gather Data
	bookingInfo = request.json
	
	# Send email to dlandry email server using client contact info
	#textClient = TextClient()

	# Return status code
	return "200"


# Run app on 0.0.0.0:5001
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5001))
	app.run(host='0.0.0.0', port=port)
