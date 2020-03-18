FROM python:3

MAINTAINER Grisha Andreev <grisha.andreev@gmail.com>

ADD metrics.py /

RUN pip install psutil

ENTRYPOINT [ "python", "./metrics.py" ]
