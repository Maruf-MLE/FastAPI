from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: int

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'naogaon', 'state': 'rajshahi', 'pin': 1024}

address1 = Address(**address_dict)

patient_dict = {'name': 'maruf', 'gender': 'male', 'age': 30, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)

# temp = patient1.model_dump()
temp = patient1.model_dump_json(include=['name','gender'])
print(temp)
print(type(temp))
