FROM node:12-alpine3.11 

WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install 

COPY . .

# RUN npm run build

# FROM nginx:1.16.0-alpine
# COPY --from=builder /usr/src/public /usr/share/nginx/html
# RUN rm /etc/nginx/conf.d/default.conf
# COPY conf/nginx.conf /etc/nginx/conf.d
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]

