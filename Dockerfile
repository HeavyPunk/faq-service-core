FROM python:3.7-buster
COPY ./ /usr/src/
EXPOSE 5123
WORKDIR /usr/src/
RUN pip install -r requirements.txt
CMD python main.py
