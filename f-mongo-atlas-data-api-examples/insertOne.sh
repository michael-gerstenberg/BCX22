curl --request POST \
  'https://data.mongodb-api.com/app/data-auspr/endpoint/data/beta/action/insertOne' \
  --header 'Content-Type: application/json' \
  --header 'Access-Control-Request-Headers: *' \
  --header 'api-key: ##APIKEY##' \
  --data-raw '{
      "dataSource": "DemoCluster",
      "database": "demoDataAPI",
      "collection": "events",
      "document": {
        "eventname": "Lachyoga",
        "part": "ABS",
        "values": [1,4,9,33]
      }
  }'