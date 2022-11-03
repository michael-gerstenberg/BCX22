curl --request POST \
  'https://data.mongodb-api.com/app/data-auspr/endpoint/data/beta/action/insertMany' \
  --header 'Content-Type: application/json' \
  --header 'Access-Control-Request-Headers: *' \
  --header 'api-key: ##APIKEY##' \
  --data-raw '{
      "dataSource": "DemoCluster",
      "database": "demoDataAPI",
      "collection": "people",
      "documents": [
        { "name": "Nina Power", "age": 34 },
        { "name": "Thomas Fast", "age": 29 },
        { "name": "Peter Cool", "age": 39 }
      ]
  }'