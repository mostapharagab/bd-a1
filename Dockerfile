
FROM ubuntu


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-setuptools

RUN pip3 install pandas numpy matplotlib scikit-learn 


RUN mkdir -p /home/doc-bd-a1


WORKDIR /home/doc-bd-a1


COPY . /home/doc-bd-a1/


CMD ["python3", "load.py"]
