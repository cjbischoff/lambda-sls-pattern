FROM python:3.8-buster
COPY . .
RUN pip install -r test/requirements.txt
CMD python -m unittest discover test
