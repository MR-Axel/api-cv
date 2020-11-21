#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, abort
from flask_mail import Mail, Message
import mail_config

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

mail = Mail(app)

app.config['MAIL_SERVER'] = mail_config.mail_server
app.config['MAIL_PORT'] =  mail_config.port_number
app.config['MAIL_USERNAME'] = mail_config.mail_username
app.config['MAIL_PASSWORD'] = mail_config.mail_password
app.config['MAIL_USE_TLS'] = mail_config.mail_use_tls
app.config['MAIL_USE_SSL'] = mail_config.mail_use_ssl


@app.route('/')
def index():
    info = {
        "message": "Welcome to the Axel CV API",
        "actions": [
            "GET /curriculum",
            "POST /message"
        ]
    }
    return jsonify(info)


@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/myPhoto.jpg"
    cv = {
        "name": "Axel",
        "lastname": "Rosso",
        "country": "Argentina",

        "experience": [{
            "position": "QA Analyst",
            "company": "Centro de Gestión de Proyectos UNSAM",
            "from": "Nov 2017",
            "to": "Present",
            "description": "Use Cases and Requirements design based on documentation and/or systems. // Test Case design and execution. // Test results analysis for reporting. // Defect logging and tracking through its life cycle. // Documentation composition for testing audits. // SQL queries to check and analize Data Bases // Perform testing in different systems and platforms (Windows, Android, DB, Web and external Hardware) // Functional: Integration, Smoke, Regression, End-To-End and UI/UX Testing. // Non-Functional: Stored Procedure, API, Stress, Load and Performance Testing. // Customer areas: Cardiology, energy, education and genomic medicine. // Customer areas: Cardiology, Energy, Education and Genomic Medicine. // Tools: Enterprise Architect 10, Redmine, Testlink, Postman, SSMS, Jmeter, DBeaver, Gitlab, Tortoise."
        },

        {
            "position": "Product Manager and QA Lead",
            "company": "Freelance",
            "from": "Feb 2020",
            "to": "Present",
            "description": "Review, define and design standard processes and UML diagrams. // Design requirements and use cases. // Prioritize tasks and allocate resources to them. // Monitor system evolution through SDLC. // Lead training related to work methodologies and tools. // Review UX for optimization. // Research market and innovations. // Hire contractors and monitor their work. // People in charge: 6 (Analysis, Development and Testing). // Tools: Microsoft Office, Enterprise Architect 13, GitHub, Testlink, Trello. // Ad honorem in a Management Systems Development startup, with eventual systems on request."
        },

        {
            "position": "Computer Technician",
            "company": "Freelance",
            "from": "Feb 2011",
            "to": "Feb 2020",
            "description": "Provision of repair and maintenance services for computers, networks and cell phones. // Remote solutions via TeamViewer. // Both private and business clients. // Computer and programming logic classes."
        }
        ],

        "education": [{
            "level": "Degree",
            "title": "IT Management",
            "institute": "UADE",
            "from": "March 2021"
        },

        {
            "level": "Degree",
            "title": "Biomedical Engineer",
            "institute": "UNSAM",
            "from": "March 2016",
            "to": "Nov 2019 "
        },

        {
            "level": "High School",
            "title": "Computer Technician",
            "institute": "E.T. Nº 35 'Ing. Eduardo Latzina'",
            "from": "March 2005",
            "to": "Nov 2011 "
        }
        ],

        "interests": ["python", "data", "QA", "product management"],
        "webs": {
            "github": "https://github.com/MR-Axel",
            "linkedin": "https://www.linkedin.com/in/axelrosso/"
        },
        "photo": url_imagen
    }
    return jsonify(cv)


def sendMessage(mensaje):
    #TODO: Connect to mail account
    try:
        msg = Message("New message from API CV",
            sender = mail_config.mail_username,
            recipients = [mail_config.mail_username])
        msg.body = mensaje
        mail.send(msg)
        print("CONTACT MESSAGE: " + str(mensaje))
        return True
    except:
        return False


@app.route('/message', methods=['POST'])
def contact():
    mensaje = request.get_data()

    if not mensaje:
        abort(400, description="You must send the message in the body of the POST")

    if (sendMessage(mensaje)):
        return "Thanks for your message."
    else:
        return "Error: Try later!"

if __name__ == "__main__":
    app.run(debug = True)
