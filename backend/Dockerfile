FROM python:3.9-buster
ENV PROJECT_ROOTDIR /app

WORKDIR ${PROJECT_ROOTDIR}

COPY backend/requirements.txt ${PROJECT_ROOTDIR}/
COPY . ${PROJECT_ROOTDIR}/
RUN pip install -r backend/requirements.txt
