from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://jai:jai@cluster0.ax3qe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["bakery"]
users = db["users"]
orders = db["orders"]

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")#[:-2]
    res = MessagingResponse()
    user = users.find_one({"number": number})
    print(user)
    print("--1")
    if bool(user) == False:
        print( "--2" )
        msg = res.message(
            "Hi, " + number +" Thanks for contacting *Shashinath Thakur*.\nYou can choose from one of the options below: "
            "\n\n*Type*\n\n 1.To *contact* us \n 2.To *buy* policy \n 3.To know our *working hours* \n "
            "4.To get our *address* \n 5.Company Profile \n ️6.Vision And Mission \n 7.Financial Advisor Team \n "
            "8.Special Products And Info \n 9.Client Testimonials \n 10.Achievements")
        #msg.media("https://i.ibb.co/BPKnXVP/Red-Velvet-Cake-Waldorf-Astoria.jpg")
        msg.media("https://9efcbb480425.ngrok.app/Images/ShashiNath.jpg")
        users.insert_one({"number": number, "status": "main", "messages": []})
        print( "3" )
        return str( res )
    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            msg = res.message(
                "Hi, " + number +" Thanks for contacting *Shashinath Thakur*.\nYou can choose from one of the options below: "
                "\n\n*Type*\n\n 1.To *contact* us \n 2.To *buy* policy \n 3.To know our *working hours* \n "
                "4.To get our *address* \n 5.Company Profile \n ️6.Vision And Mission \n 7.Financial Advisor Team \n "
                "8.Special Products And Info ") #\n 9.Client Testimonials \n 10.Achievements")
            #msg.media("https://9efcbb480425.ngrok.app/Images/ShashiNath.jpg")
            users.insert_one({"number": number, "status": "main", "messages": []})
            res.message("Please enter a valid response ")
            print("inside except")
            return str(res)

        if option == 1:
            res.message(
                "You can contact us through phone or E-Mail.\n\n*Phone*: 09821265766 \n*E-mail* : nath@nathinvestment.in")
        elif option == 2:
            res.message("You have entered *buy policies*.")
            #users.update_one(
            #   {"number": number}, {"$set": {"status": "ordering"}})
            res.message(" we will soon contact you on this number-" + number )
        elif option == 3:
            res.message("We work from *9 a.m. to 5 p.m*."
                        )
        elif option == 4:
            res.message(
                "We have multiple offices across the city. Our main center is at sector 21 Nerul east new Mumbai")
        elif option == 5:
            res.message(
                "I am Shashi Nath Thakur , having a small attempt from my side to provide my all customers , "
                "with accurate information and services they might require at their fingertips at a time of their "
                "convenience."
                "\n A Graduate. I have been working as a customer-focused adviser for 22 years  "
                "\n I believe in keeping myself continuously updated with a strong regimen of self-study and "
                "\n engagement in industry-level training and seminars"
                "\n Through this I am able to ensure a relevant and current advisory for my clients at all time"
                "\n I also mentor my team on a regular basis to maintain their excellence levels perhaps that is also "
                "one of the reason that we currently service many policies & providing services to huge policy "
                "holders with ease."
                )
        elif option == 6:
            res.message(
                "Our vision is to provide all our customers a one stop solution to all their insurance and investement related problems"
                "\n and all the hurdles faced by them during claim processing of losing their loved ones."
                "\n As advisors, consultants, friends and family we will always be with them"
                "\n This way we want to make our near and dear ones and people around us financially free"
                "\n and our vision is to reach top at table in serving our users and customers"
                "\n\n\n I am Shashinath Thakur and my mission is to guide 100000 families lead a dignified life"
            )
        elif option == 7:
            res.message("1.Anil Jha  (LIC , SBA &DO) \n\n 2.ShashiNath Thakur (Head Financial Advisor)"
                         "\n\n 3.Kshitij Waldiya( Health Advisor Star Health)"
            )
        elif option == 8:
            res.message( "We deal mainly in \n 1.Car Insurance \n 2.Health Insurance \n 3.Life Insurance \n 4.Mutual Funds"
                        )
    else:
            print("---5")
            msg = res.message(
                "Hi, " + number + " Thanks for contacting *Shashinath Thakur*.\nYou can choose from one of the options below: "
                                  "\n\n*Type*\n\n 1.To *contact* us \n 2.To *buy* policy \n 3.To know our *working hours* \n "
                                  "4.To get our *address* \n 5.Company Profile \n ️6.Vision And Mission 7.Financial Advisor Team \n "
                                  "8.Special Products And Info \n 9.Client Testimonials 10.Achievements" )
            msg.media( "https://9efcbb480425.ngrok.app/Images/ShashiNath.jpg" )
            users.update_one(
               {"number": number}, {"$set": {"status": "main"}})
            print( "---6" )
            print( user )

            res.message("Please enter a valid response")
    return str(res)

if __name__ == "__main__":
    app.run()
