import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str, mock:bool = False)->dict[str,str]:
    if mock:
        linkedin_profile_url= "https://gist.githubusercontent.com/feliperod0519/2498b17130171be7097c6ccba70303fd/raw/640bd414c414ddb57d553794174110e124e88034/some-person.json"
        response = requests.get(linkedin_profile_url,timeout=20)
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey":os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url
        }
        response = requests.get(api_endpoint,params=params,timeout=20)
    data = response.json().get("person")
    newData = { 
                k: v
                for k,v in data.items()
                if v not in ([],"", "", None) and k not in ['certifications']
              }
    # for k,v in data.items():
    #     print(f'{k}')
    
    #print(newData)
    return newData

if __name__ == "__main__":
   print(scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/nataliawiechowski/",mock=True))