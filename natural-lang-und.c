curl -X POST -u "apikey:insertKey" \
--header "Content-Type: application/json" \
--data '{
  "text": "I stay in Block 123 Yishun Ring Road",
  "features": {

    "sentiment": {
      "targets": [
        "Block 123 Yishun Ring Road",
        "Block 123 Bedok Road",
        "Block 122 Yishun Ring Road"
      ]
    },
    "keywords": {
      "emotion": false
    }
  }
}' \
"insertURL/instances/71dd1904-c98f-4be6-bbdf-762ea3220067/v1/analyze?version=2019-07-12"

/*under targets, strings of each possible address in database of singapore address will be included.
/*through this, if the keyword of that address is identified in "text", this keyword will be raised as the location of caller.