from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email:EmailStr
    age:int
    weight: float # kg
    height: float # mtr
    married: Optional[bool] = None
    allergies: Optional[List[str]] = None
    contact_details:Dict[str,str]


    @computed_field
    @property   
    def bmi(self) -> float:
        bmi_result = round(self.weight/(self.height**2),2)
        return bmi_result

    
def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(type(patient.weight))
    print('BMI',patient.bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@cnpi.com', 'linkedin_url':'linkedin.com/1322', 'age': '30', 'weight': 75.2,'height':1.72,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)


    