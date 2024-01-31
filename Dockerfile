# Use an official PHP image with Apache
FROM php:8.0-apache

# Install Python and necessary tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python

# Copy your project files into the container
COPY . /var/www/html

# If you have a requirements.txt for Python dependencies, install them
# COPY py/requirements.txt /tmp/
# RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Enable Apache mod_rewrite for .htaccess support
RUN a2enmod rewrite

# Set ServerName to suppress Apache warning
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Expose port 80 for the Apache server
EXPOSE 80

# Start Apache in the foreground
CMD ["apache2-foreground"]
