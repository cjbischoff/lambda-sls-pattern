FROM nikolaik/python-nodejs:python3.8-nodejs14

RUN npm install -g serverless@2.8.0

RUN mkdir -p /srv

WORKDIR /srv

COPY . .

RUN pip install -U pip

RUN pip install -r requirements.txt --upgrade --no-cache-dir
