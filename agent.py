from kerykeion import AstrologicalSubject, KerykeionChartSVG, Report
from datetime import datetime

import google.generativeai as genai
import os
from brain import json
from brain import examples
from dotenv import load_dotenv



# Configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-1.5-flash") 


def agent(Name, birth_date, birth_time,birth_city, birth_country,question):
    birth_datetime_str = f"{birth_date} {birth_time}"
    birth_datetime = datetime.strptime(birth_datetime_str,"%Y-%m-%d %H:%M")
    year = birth_datetime.year
    month = birth_datetime.month
    day = birth_datetime.day
    hour = birth_datetime.hour
    minute = birth_datetime.minute
    subject = AstrologicalSubject(Name,year, month, day, hour, minute,birth_city,birth_country)
   # report = Report(subject)
   # report.print_report()
    dict = {
        "sun": [subject.sun.sign, subject.sun.position,subject.sun.house],
        "moon": [subject.moon.sign, subject.moon.position,subject.moon.house],
        "mercury": [subject.mercury.sign, subject.mercury.position,subject.mercury.house],
        "venus": [subject.venus.sign, subject.venus.position,subject.venus.house],
        "mars": [subject.mars.sign, subject.mars.position,subject.mars.house],
        "jupiter": [subject.jupiter.sign, subject.jupiter.position,subject.jupiter.house],
        "saturn": [subject.saturn.sign, subject.saturn.position,subject.saturn.house],
        "uranus": [subject.uranus.sign, subject.uranus.position,subject.uranus.house],
        "neptune": [subject.neptune.sign, subject.neptune.position,subject.neptune.house],
        "pluto": [subject.pluto.sign, subject.pluto.position,subject.pluto.house],
        "mean_node": [subject.mean_node.sign, subject.mean_node.position,subject.mean_node.house],
        "true_node": [subject.true_node.sign, subject.true_node.position,subject.true_node.house],
        "mean_south_node": [subject.mean_south_node.sign, subject.mean_south_node.position,subject.mean_south_node.house],
        "true_south_node": [subject.true_south_node.sign, subject.true_south_node.position,subject.true_south_node.house],
        "chiron": [subject.chiron.sign, subject.chiron.position,subject.chiron.house],
        
            }
    prompt = f""" You are an AI astrologer agent. You have to generate predictions for the user according to the following data 
         
                {json}    
                
                The astrological data of user is as follows: {dict}

                generate the response according to the following examples : {examples}
                 
                and answer the following question as shown in the examples {question}
                
                keep your response brief.
                   
                   """
    

    response = model.generate_content(prompt)
    reading = response.text

    return reading