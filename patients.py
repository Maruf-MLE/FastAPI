from fastapi import FastAPI,Path,HTTPException,Query
import json
app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data



@app.get("/")
def hello():
    return {'message':'Patients Management system API'}


@app.get("/about")
def about():
    return {'message':'A fully funtional API to manage your patients records'}


@app.get('/vew')
def vew():
    data = load_data()
    return data

@app.get('/vew/{patient_id}')
def vew_patient(patient_id:str=Path(...,description="This is e path for patient id",example="P001")):
    #load all patient
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    # return {'error':'patient not found'}
    raise HTTPException(Status_code=404,detail='Patient not found')


@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description="Sort on the bassis of height ",
),order:str=Query('asc',description='sort basis of order and it is optional')):

    valid_fields=['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=4000,detail='invalid field select from{valid_fields}')

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='invalid order,select please select asc or desc')

    data= load_data()

    sort_order=True if order=="desc" else False 

    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by,0),reverse=sort_order)

    return sorted_data