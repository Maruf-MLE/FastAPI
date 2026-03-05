from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email:EmailStr
    age:int
    weight: float
    married: Optional[bool] = None
    allergies: Optional[List[str]] = None
    contact_details:str


    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return self
    
def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(type(patient.weight))
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@cnpi.com', 'linkedin_url':'linkedin.com/1322', 'age': '40', 'weight': '75.2','contact_details':'emergency'}

patient1 = Patient(**patient_info)

update_patient_data(patient1)


