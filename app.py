import os
from dotenv import load_dotenv
import openai 
import json

load_dotenv()
key=os.getenv('OPENAI_API_KEY')
openai.api_key=key

def generate_data(prompt,no_of_data):
    icecream_data=[]
    
    for i in range(no_of_data):

        content_generated=False

        while not content_generated:
            # We may get error openai_object_classes we should install openai==0.28
            response=openai.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role':'system','content':'you are a helpfull assistent'},
                    {'role':'user','content':prompt}
                ],
                max_tokens=130,
                temperature=0.7,
                top_p=1
            )
        

            messages=response.choices[0].message.content
            messages=messages.strip().split()

            #word_count=len(messages.split())

            #if word_count>=70 and word_count<=150:
            icecream_data.append(messages)
            content_generated=True
            
        prompt+="Generate another response "
        
    return icecream_data

def save_data(data):
    with open('icecream_data.json','w') as f:
        json.dump(data,f)


# Generate the syntetic data using open based on the prompt ice cream sales data 

prompt="""
    Generate  ice cream sales data in json format
    #################################################

    ice cream name, price, perday_sales,season,year,month,location,review

    review it should fill with balance tokens
    """
no_of_data=2

data=generate_data(prompt,no_of_data)
save_data(data)
print("done with ice cream")