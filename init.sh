
ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart


ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
gunicorn --workers=2 --bind=0.0.0.0:8080 hello:app
/etc/init.d/gunicorn restart






