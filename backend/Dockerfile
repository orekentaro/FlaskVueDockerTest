FROM python:3.9-buster
ENV PROJECT_ROOTDIR /app/FlaskVueTest/backend

WORKDIR ${PROJECT_ROOTDIR}

# COPY requirements.txt ${PROJECT_ROOTDIR}/
COPY . ${PROJECT_ROOTDIR}/
RUN cd backend && pip install -r requirements.txt

CMD ["python", "app.py"]