# Sample API for report application status via JSON document 

This API has two endpoints:

* healthz
  returns 200 and json string indicating health of API
* status
  returns 200 + json doc if it can find a given JSON document
  returns 404 if it cannot find the document
