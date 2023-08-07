
## Authors



# TextAnalysis

This Project is all about text analysis using pre-trained Model.
project is divided in to 4 microservices based on python fastapi, Mongodb to store data.

Microservices are listed below:

  1. **Central Service:** This is a central microservice which manages the  different text analysis services.
  2. **Sentiment Analysis Service:** This service analyzes the sentiment of the text (positive, neutral, negative).
  3. **Word Count Service:** This service counts the number of words in the text.
  4. **Entity Recognition Service:** This service identifies and classifies named entities (e.g., persons, organizations, locations) in the text.


## Documentation


***To Run This Project Locally Do The Below Steps**

1. Create One MongoDb Database Which Name Should Be "**service_registry_db**"
2. After That Create One Mongodb Collection Which Name Should Be **"services"**
***When You Create Service Make Sure You Give Name And Url According To This Documentation**
1. **For Sentiment Analysis**

    {

      "name": "sentiment-analysis",

      "url": "http://localhost:8001/analyze"

    }
2. **For Word Count Analysis**

    {

      "name": "word-count",

      "url": "http://localhost:8002/count"

    }

3. **For Entity Recognition Analysis**

    {

      "name": "entity-recognition",

      "url": "http://localhost:8003/recognize"

    }

## API Reference

#### Get all items

```http
  GET /service/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
|  |  |  No Parameter Is Required|

#### Create service
```http
  POST /service/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`    | `string` | **Required**.Provide service name|
|  `url`    |`string`  |**Required**. URL of service 

```http
  POST /analyze/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `service`    | `string` | **Required**. service name you want to invoke|
|  `text`    |`string`  |**Required**. Provide Any Text Data to perform analysis on it 


## Run Locally

Clone the project

```bash
  git clone "project repo"
```

Go to the project directory

```bash
  cd test
```

Install dependencies

```bash
  pip install -r requirements.txt
  
  python -m spacy download en_core_web_md

```

Start the server(central_microservice)

```bash
  uvicorn main:app --host localhost --port 8000
```
Start the server(sentiment_analysis_service)

```bash
  uvicorn main:app --host localhost --port 8001
```
Start the server(word_count_service)

```bash
  uvicorn main:app --host localhost --port 8002
```
Start the server(entity_recognition_service)

```bash
  uvicorn main:app --host localhost --port 8003
```

