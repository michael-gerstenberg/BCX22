curl --request POST \
  'https://data.mongodb-api.com/app/data-auspr/endpoint/data/beta/action/findOne' \
  --header 'Content-Type: application/json' \
  --header 'Access-Control-Request-Headers: *' \
  --header 'api-key: ##APIKEY##' \
  --data-raw '{
      "dataSource": "DemoCluster",
      "database": "demoDataAPI",
      "collection": "people",
      "filter": { "name": "Michael Power" }
  }'w