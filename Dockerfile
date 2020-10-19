FROM frolvlad/alpine-glibc:alpine-3.8
MAINTAINER whq <krman#163.com>
 
COPY ./dist/server    /server
 
ENV TZ=Asia/Shanghai

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk add --no-cache tzdata bash && rm -rf /var/cache/apk/*
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone

WORKDIR /server
 
EXPOSE 5000
CMD /server/server