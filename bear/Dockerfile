# remove .amd64 if you are not on a macbook with a M1/M2 processor
FROM python:latest

# add requirements.txt file
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
# install pip and install libraries
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
# add main.py file
COPY ./main.py /code/
# add bear_facts.txt file
COPY ./bear_facts.txt /code/
# run main.py using python
CMD ["python", "main.py"]



