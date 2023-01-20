"""FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /findpdf
WORKDIR /findpdf
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]

#test failed
Expose 3306"""

FROM python:3.10
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]

