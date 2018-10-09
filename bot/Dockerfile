FROM python:3.7.0-stretch
RUN pip install zope.interface constantly incremental attrs Automat twisted pymodbus3 pendulum redis influxdb msgpack-python toml python-etcd falcon waitress greenlet gevent logbook
RUN pip install python-telegram-bot
RUN pip install beautifulsoup4
COPY . /app/
WORKDIR /app/
CMD python /app/reddit.py && python bot.py