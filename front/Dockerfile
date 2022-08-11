FROM node:16.6.1-alpine
ENV PROJECT_ROOTDIR /app
WORKDIR ${PROJECT_ROOTDIR}

COPY package*.json ${PROJECT_ROOTDIR}/
COPY . ${PROJECT_ROOTDIR}/

RUN cd front && npm install --frozen-lockfile
CMD ["npm", "run", "dev"]