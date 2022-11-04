# Get started with MongoDB Atlas

__Here you get an overview how to use and integrate a MongoDB Atlas Cluster incl. all Services into your architecture and how to download the Bosch Building Technology Dataset.__

__In case you have questions, don't hesitate to contact us via__: 
* [Michael Gerstenberg](mailto:michael.gerstenberg@mongodb.com)
* [Celia Halenke](celia.halenke@mongodb.com)
* [Max Marcon](massimiliano.marcon@mongodb.com)
* [Niklas Kazal](niklas.kazal@mongodb.com)

__We are only here to support you and make you successful the hackathon!__

Below is a list of selected topics. MongoDB Atlas is a Developer Platform which is there to make you as fast as possible, so perfect for a hackathon! There are so many features included in MongoDB Atlas like Visualizations, Fulltext Search, APIs like GraphQL ... So we recommend to contact us as early as possible so you can leverage as much of the MongoDB Atlas Platform as possible and you don't waste time!

Everything you can see here in the green box is provided by MongoDB Atlas.

![](images/atlas_overview.png "Atlas Overview")

---
## Topics

__Initial Setup__

* How to create a MongoDB Atlas Cluster (see down)
* Overview of MongoDB Atlas Services (see down) (mach ich in dem pitch morgen fr)
* How to download sample Bosch Building Technology data set (see down)
* How to manage MongoDB Atlas Clusters: [API Examples](f-mongo-atlas-api-examples) | [Terraform Examples](f-mongo-atlas-terraform) | [Terraform Docs](https://registry.terraform.io/providers/mongodb/mongodbatlas/latest/docs)

__Architecture__

* [MongoDB Atlas Architecture Guide](https://www.mongodb.com/cloud-explained/cloud-architecture)
* [MongoDB & AWS reference architectures](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/architecture.html)
* [MongoDB & Azure reference architectures](https://learn.microsoft.com/en-us/azure/architecture/browse/?terms=mongo)

__Azure & AWS Integrations__

* For Kafka, Azure Eventhub & AWS EventBridge look at the topic Real Time/CDC
* How to connect to Azure Power Platform: [Detailed Instruction](https://github.com/microsoft/PowerPlatformConnectors/tree/master/certified-connectors/MongoDB) | [Azure Docs](https://learn.microsoft.com/en-us/connectors/custom-connectors/define-blank)
* How to create Cluster with Azure Link: [Example](https://github.com/eugenebogaart/Atlas-Azure-Link)
* How to create Cluster with AWS Link: [Example](https://github.com/eugenebogaart/Atlas-AWS-Link)

__Other Integrations__

* How to connect with SQL/JDBC/ODBC and BI Tools (SQL Workbench, Power BI, Tableau, Qlik...): [Atlas SQL Product Page](https://www.mongodb.com/atlas/sql) | [BI Connector](https://www.mongodb.com/docs/atlas/bi-connection/)
* How to connect with Spark for ML/AI: [Information Page](https://www.mongodb.com/products/spark-connector)

__Real Time/Change Data Capture__

* How to connect to Kafka: [Documentation](https://www.mongodb.com/docs/kafka-connector/current/) | [Example 1](https://github.com/mongodb/mongo-kafka) | [Example 2](https://github.com/PhilippW94/Kafka_POV#description-contents) | [Example Custom WriteStratgety](https://github.com/felixreichenbach/KafkaSinkConnectorCustomizations)
* How to handle Change Data Capture (CDC): [Examples](f-mongo-change-streams-examples)
* How to connect to Azures Eventhub: [Detailed Tutorial](https://www.mongodb.com/blog/post/using-azure-event-hubs-with-connector-apache-kafka) | [Sample Code](https://github.com/RWaltersMA/azure-event-hubs-mongo)
* How to connect to AWS Event Bridge for CDC: [Tutorial](https://www.mongodb.com/docs/atlas/triggers/eventbridge/)

__Interfaces/APIs__

* How to connect with Spark: [Documentation](https://www.mongodb.com/docs/spark-connector/current/)
* How to create HTTP(S) Endpoints: [Documentation](https://www.mongodb.com/docs/atlas/app-services/data-api/custom-endpoints/) 
* How to deploy a GraphQL API: [Documentation & Examples](https://www.mongodb.com/docs/atlas/app-services/graphql/)
* How to use MongoDB Atlas Data API (HTTP requests): [Examples](f-mongo-atlas-data-api-examples) | [Atlas Docs](https://www.mongodb.com/docs/atlas/api/data-api/)

__MongoDB (Atlas) Features__

* How to implement Fulltext-Search capabilities like Fuzzy Search, Highlighting, Autocomplete ...: [Fulltext-Search Example](f-mongo-atlas-fulltext-search) | [Autocomplete Example](f-mongo-atlas-auto-complete)
* How to create Visualizations/Charts and embedd them: [Documentation incl. Examples](https://www.mongodb.com/docs/charts/)
* How to traverse Graphs with MongoDB: [Example](https://github.com/pkdone/GraphPersonsAndPlaces)
* How to store Files/Binary Data in MongoDB: [Example Application](f-mongo-store-binary-example-app/)
* How to handle Time Series Data: [Docs](https://www.mongodb.com/docs/manual/core/timeseries-collections/) | [Examples](f-mongo-time-series-examples)
* How to use things you know from relational databases: [Example for Joins](https://www.stackchief.com/tutorials/%24lookup%20Examples%20%7C%20MongoDB) | [Atlas Docs incl. Example](https://www.mongodb.com/docs/manual/reference/method/Session.startTransaction/)
* How to create a mobile application including mobile device sync: [Docs incl. Example with different SDKs](https://www.mongodb.com/docs/realm/)

__Diverse__

* [More topics](https://github.com/michael-gerstenberg/BCX22)

## Create a MongoDB Atlas Cluster

* Register yourself for an Atlas account [here](https://www.mongodb.com/cloud/atlas/register) or login to your existing Atlas account
* Head to the billing page in Atlas and get your Atlas credits by applying the code MKT-BCX22-1122 on the lower section of the billing overview: [documentation](https://www.mongodb.com/docs/atlas/billing/subscriptions/)
* Create your first MongoDB cluster: [Documentation](https://www.mongodb.com/docs/atlas/tutorial/create-new-cluster/)
* Whitelist your connection IP address and add your first database user: [Documentation](https://www.mongodb.com/docs/atlas/security/add-ip-address-to-list/)
* Connect to your cluster: [Documentation](https://www.mongodb.com/docs/atlas/tutorial/connect-to-your-cluster/) 


## Download the Bosch Bulding Technology Data Set

We prepared a data set from Boch Building Technologies. You can download that from a public S3 bucket and use mongorestore to load it onto your cluster. To do so follow the following steps.

You can easily do that with wget. If you don't have it you can use brew ```brew install wget``` with your MacBook. After that unzip the file.

```
wget https://geegeedemo.s3.eu-central-1.amazonaws.com/BCX22/mongo-dump.zip
```

This download includes two collections. Both collections have exactly the same data included. One is a MongoDBs Time Series collection the the other is a normal collection. You can choose on your own what you wish to use.

To restore those collections on your Atlas Cluster use the following command. Switch first into the ```mongo-dump``` folder. Replace the username, password and host with your user and host. You need to restore the dataset onto the Primary Node of MongoDB Atlas. To figure out which one is the current primary log into the Atlas UI and click on the Cluster name. There you see all Nodes and in this example the primary is the second in the list with the name __bcx22-shard-00-01.da1ep.mongodb.net:27017__. As soon as you hover over the name you can copy the complete hostname.

```
mongorestore --host {hostname}  --authenticationDatabase admin --ssl --username {username} --password {password} --nsExclude "admin.system.*" --nsInclude "BCX22.*"
```

Example:

```
mongorestore --host bcx22-shard-00-01.da1ep.mongodb.net:27017  --authenticationDatabase admin --ssl --username michael --password iev72nivnbw99 --nsExclude "admin.system.*" --nsInclude "BCX22.*"
```

After that the dataset is restored onto your cluster.


Todos:
- api examples doent work
- ts examples

