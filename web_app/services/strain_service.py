import requests
import json

url_strains = "https://raw.githubusercontent.com/bw-ft-medcab3-brian/ds/master/schemas/json_example_schema.txt"
result = requests.get(url_strains)
strains = json.loads(result.text)

#import pdb; breakpoint()


#from services.strain_service import strains