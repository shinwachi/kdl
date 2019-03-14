FROM ubuntu:18.04
# alpine failed to run knime

RUN apt-get update
RUN apt-get install -y openjdk-11-jre
RUN apt-get update  && apt install -y software-properties-common && add-apt-repository -y ppa:deadsnakes/ppa && apt install -y python3.7
RUN apt-get install -y python3-pip && pip3 install flask simplejson
RUN apt-get install -y wget

# shamelessly stolen from https://github.com/DrSnowbird/knime-docker/blob/master/Dockerfile
ARG PRODUCT=${PRODUCT:-knime}
ENV PRODUCT=knime
ARG PRODUCT_VERSION=${PRODUCT_VERSION:-3.7.1}
ENV PRODUCT_VERSION=${PRODUCT_VERSION}
ARG PRODUCT_DIR=${PRODUCT_DIR:-knime_${PRODUCT_VERSION}}
ENV PRODUCT_DIR=${PRODUCT_DIR}
ENV DOWNLOAD_URL=https://download.knime.org/analytics-platform/linux/${PRODUCT}_${PRODUCT_VERSION}.linux.gtk.x86_64.tar.gz
#### ---- Install for application ----
RUN wget -c ${DOWNLOAD_URL} && \
    tar xvf $(basename ${DOWNLOAD_URL}) && \
    rm $(basename ${DOWNLOAD_URL} )

COPY ./server /server
COPY ./worker /worker

RUN apt-get install -y git
RUN git clone https://github.com/knime-dsl/kdl.git
RUN echo 'alias python3=python3.7' >  ~/.bashrc

# RUN cd /kdl && pip3 install -r requirements.txt && python3.7 setup.py install
CMD ["/bin/bash", "/server/run_server.sh"]