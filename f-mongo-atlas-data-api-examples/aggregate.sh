curl --request POST \
  'https://data.mongodb-api.com/app/data-auspr/endpoint/data/beta/action/aggregate' \
  --header 'Content-Type: application/json' \
  --header 'Access-Control-Request-Headers: *' \
  --header 'api-key: ##APIKEY##' \
  --data-raw '{
      "dataSource": "DemoCluster",
      "database": "demoDataAPI",
      "collection": "people",
      "pipeline": [
        {
          "$match": {
            "name": "Michael Power"
          }
        }
      ]
  }'