FROM php:7.4-fpm

WORKDIR /var/www

RUN apt update
RUN apt install libcurl4-openssl-dev pkg-config libssl-dev unzip -y
RUN pecl install mongodb
RUN docker-php-ext-enable mongodb.so

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer require mongodb/mongodb
