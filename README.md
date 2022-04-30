# Welcome Fullstack Flutter with FastAPI Inventory workshop 2022

## Official Page
[FastAPI](https://fastapi.tiangolo.com/)
## Config and Setup tools
### Python ENV
* config python env
    `python -m venv env`
* Activate env
    `.\env\Scripts\activate`

### How to run server
`uvicorn main:app --reload`

## Libraries
* fastapi `pip install fastapi`
* uvicorn `pip install "uvicorn[standard]"`
* black `pip install black`
* sqlalchemy `pip install sqlalchemy`
* python-jose `pip install python-jose`
* decouple `pip install python-decouple`
* psycopg2 `pip install psycopg2`
* python-multipart `pip install python-multipart`

## Black formatter
[black doc](https://github.com/psf/black)

## Sqlalchemy
* [Docs](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)

### CORS 
* [Ref](https://fastapi.tiangolo.com/tutorial/cors/)

### Oauth2 [Ref](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
* python-jose `pip install python-jose`
    * [Ref](https://github.com/mpdavis/python-jose)
* passlib `pip install passlib`
* bcrypt `pip install bcrypt`

## Generate key by openssl
* cli `openssl rand -hex 32`

## Ref. Document
* [What's MVC](https://medium.com/computer-science-kmitl/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%99%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B9%81%E0%B8%9A%E0%B8%9A-mvc-%E0%B8%84%E0%B8%B7%E0%B8%AD%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3-57112d932dde)
* [JWT](https://medium.com/rootusercc/json-web-token-%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%A3%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B9%83%E0%B8%AB%E0%B8%A1%E0%B9%88-%E0%B9%83%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%B3-authentication-b0760dd9acd1)

* [JWT 2](https://www.devahoy.com/blog/2016/07/understanding-token-and-jwt-create-authentication-with-hapijs)

* [FastAPI deploy to heroku](https://stackoverflow.com/questions/68600980/deploying-fastapi-to-heroku-fails)