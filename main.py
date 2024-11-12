#import library
#fastApi > class
from fastapi import FastAPI, HTTPException, Header
import pandas as pd

#create instance/object
app = FastAPI()



#define API KEY (1)
apiKey = "test123"

#define endpoint home (2A)
@app.get("/")
def root():
    return {"message": "halo!"}

#define url -> endpoint (2B)
@app.get("/protected")
def root(key: str = Header(None)):
    if key == None or key != apiKey:
        raise HTTPException(status_code=401, detail="key tidak sesuai!")
    #get all data from datafram
    df = pd.read_csv("data.csv")
    return filter.to_dict(orient='records')

@app.get("/data/{id}")
def get_data_by_id(id: int):
    df = pd.read_csv("data.csv")

    #untuk filtering -> df[kondisi], df.query(kondisi)
    #untuk manggil kolom -> df[id], df.id
    filter = df[df.id == id]

    #condition if else for filter
    #if our data is not found or there is no match data
    if len(filter) == 0:
        #return pesan error
        raise HTTPException(status_code = 404, detail = 'data tidak ditemukan')
    #if our data is found
    else:
        return filter.to_dict(orient='records') # / to_json()

@app.get("/data")
def get_data():
    df = pd.read_csv("data.csv")
    #convert df to dict
    return df.to_dict(orient='records') # / to_json()

@app.get("/data/{fullname}")
def get_data_by_id(fullname: str):
    df = pd.read_csv("data.csv")

    #untuk filtering -> df[kondisi], df.query(kondisi)
    #untuk manggil kolom -> df[id], df.id
    filter = df[df.fullname.str.lower() == fullname.lower()]

    #condition if else for filter
    #if our data is not found or there is no match data
    if len(filter) == 0:
        #return pesan error
        raise HTTPException(status_code = 404, detail = 'data tidak ditemukan')
    #if our data is found
    else:
        return filter.to_dict(orient='records') # / to_json()

# @app.post('/input_data/')
# def add_data(update_df:dict):

#     df = pd.read_csv('data.csv')

#     # define new id for new data
#     id = len(df) + 1

#     #assign new id to column id in new df named update_df 
#     update_df['id'] = id

#     # create new dataframe because we will use concat
#     new_data = pd.DataFrame([update_df])

#     # concat dataframe
#     df = pd.concat([df, new_data], ignore_index=True)

#     # Save updated DataFrame back to CSV
#     df.to_csv('data.csv', index=False)

#     return df.to_dict(orient='records')