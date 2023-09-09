import requests

parameters={
    "amount":10,
     "difficulty":"easy",
    "type":"multiple"
}
response=requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
question_data =response.json()["results"]
print(question_data)
