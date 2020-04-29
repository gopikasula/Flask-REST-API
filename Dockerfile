FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 5000
# CANNOT OVERRIDE
ENTRYPOINT ["python3"]
# OVERIDABLE  
CMD ["app.py"]