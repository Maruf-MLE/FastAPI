from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the patient',
    description='Give the name of the patient in 50 char',examples=['Maruf','Nitish'])]
    email:EmailStr
    age:int
    weight:Annotated[float,Field(gt=0,strict=False)]
    married:Annotated[Optional[bool],Field(default=None,description='is the patient married or not')]
    allergies:Optional[Annotated[List[str],Field(max_length=5)]] = None
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains=['cnpi.com','duet.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value


    @field_validator('name',mode='after')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(type(patient.weight))
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@cnpi.com', 'linkedin_url':'linkedin.com/1322', 'age': '30', 'weight': '75.2','contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)


    