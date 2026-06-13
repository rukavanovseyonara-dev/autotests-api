import json

json_date = '{"name": "Ivan", "age": 30, "is_student": false}'

parsed_date = json.loads(json_date)

print (parsed_date)