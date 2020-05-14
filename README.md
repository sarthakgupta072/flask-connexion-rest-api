# A simple flask connexion REST API

### Running the app locally

```python3 -m venv env
source env/bin/activate
python3 install -r requirements.txt
python3 server.py
```

After that you can go to: 

`localhost:5000`

`localhost:5000/api/people`

To access the beautiful swagger ui, navigate here:

`http://localhost:5000/api/ui/`

If some error comes then install

`pip3 install connexion[swagger-ui]`

and again navigate to the above URL.


**NOTE: The code is well documented, so can be used as a reference**

### Why am I using connexion, when a REST API can be easily made with Flask?
The Connexion module allows a Python program to use the Swagger specification. This provides a lot of functionality: validation of input and output data to and from your API, an easy way to configure the API URL endpoints and the parameters expected, and a really nice UI interface to work with the created API and explore it.

All of this can happen when you create a configuration file your application can access. The Swagger site even provides an online configuration editor tool to help create and/or syntax check the configuration file you will create.
