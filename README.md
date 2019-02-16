# kdl



## Knime Webservice Example

In /docker folder: an example of dockerized web service which runs knime workflow.

To test the dockerized web service, use curl or postman:

```bash
curl -X POST \
  http://localhost:8080/api/v0/workflow \
  -H 'Postman-Token: 9d1a019f-fbed-4ed3-be9c-5495611bc432' \
  -H 'cache-control: no-cache' \
  -d '[ {  "Name" : "Aa",  "Type" : "a",  "Score" : 6}, {  "Name" : "Bb",  "Type" : "a",  "Score" : 3}, {  "Name" : "Cc",  "Type" : "a",  "Score" : 4}, {  "Name" : "Dd",  "Type" : "a",  "Score" : 2}, {  "Name" : "Aa",  "Type" : "b",  "Score" : 1}, {  "Name" : "Cc",  "Type" : "b",  "Score" : 9}, {  "Name" : "Dd",  "Type" : "b",  "Score" : 3} ]'
```

Output:

```json
[ {
  "Name" : "Aa",
  "a" : 6.0,
  "b" : 1.0
}, {
  "Name" : "Bb",
  "a" : 3.0
}, {
  "Name" : "Cc",
  "a" : 4.0,
  "b" : 9.0
}, {
  "Name" : "Dd",
  "a" : 2.0,
  "b" : 3.0
} ]
```