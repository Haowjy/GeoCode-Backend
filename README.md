# GeoCode-Backend

django app build by following: https://www.cockroachlabs.com/docs/v20.1/build-a-python-app-with-cockroachdb-django
## API:
```
Post http://18.222.146.208/user/
{
"uuid":"<uuid4>"
}
```
```
Post http://18.222.146.208/gps/
{
    "uuid":"<uuid4>",
    "address":"<string>",
    "city":"<string>",
    "state":"<string>",
    "zip_code":"<string>"
}
```
```
Post http://18.222.146.208/gps/
{
    "uuid":"<uuid4>",
    "score":<int>,
    "close_contact":<boolean>
}
```
```
Post http://18.222.146.208/at_risk/
{
    "address":"<string>",
    "city":"<string>",
    "state":"<string>",
    "zip_code":"<string>",
    "risk_level":<int>
}
```


```
Get http://18.222.146.208/gps/<uuid4>/
```
```
Get http://18.222.146.208/symptoms/<uuid4>/
```
```
Get http://18.222.146.208/at_risk/<address>/<zip_code>
```


## Schema:
```
user:
    column uuid UUID4 UNIQUE NOT NULL

gps:
    column uuid UUID4 NOT NULL,
    column date DATE NOT NULL,
    column address VARCHAR(50),
    column city VARCHAR(25) NOT NULL,
    column state VARCHAR(2) NOT NULL,
    column zip VARCHAR(20) NOT NULL

symptoms:
    column uuid UUID4 NOT NULL,
    column date DATE NOT NULL,
    column score INT8 NOT NULL,
    column close_contact BOOLEAN NOT NULL

at_risk:
    column date DATE NOT NULL,
    column address VARCHAR(50),
    column city VARCHAR(25) NOT NULL,
    column state VARCHAR(2) NOT NULL,
    column zip VARCHAR(20) NOT NULL,
    column risk_level INT(3) NOT NULL;
```
