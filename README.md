# GeoCode-Backend

## API:
```
Post http://18.222.146.208/user/
{
"uuid":<int>
}
```
```
Post http://18.222.146.208/gps/
{
    "uuid":<int>,
    "address":"<string>",
    "city":"<string>",
    "state":"<string>",
    "zip_code":"<string>"
}
```
```
Post http://18.222.146.208/gps/
{
    "uuid":<int>,
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
Get http://18.222.146.208/gps/<uuid>/
```
```
Get http://18.222.146.208/symptoms/<uuid>/
```
```
Get http://18.222.146.208/at_risk/<address>/<zip_code>
```


## Schema:
```
user:
    column uuid INT32 UNIQUE NOT NULL

gps:
    column uuid INT32 NOT NULL,
    column date DATE NOT NULL,
    column address VARCHAR(50),
    column city VARCHAR(25) NOT NULL,
    column state VARCHAR(2) NOT NULL,
    column zip VARCHAR(20) NOT NULL

symptoms:
    column uuid INT32 NOT NULL,
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
