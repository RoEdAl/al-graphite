# Graphite [Arch Linux packages]

1. Download (or build) and install following packages:

   * **python-whisper**,
   * **python-carbon**,
   * python-django-tagging (required by **python-graphite-web**),
   * **python-graphite-web**.

1. *Carbon* configuration:

   * Edit *Carbon's* configuration file - [`/etc/carbon/carbon.conf`](python-carbon/carbon.conf).
   
     By default *Carbon* listen **only UDP packets** on localhost.
     
   * Run Carbon server instance(s) - you have following options:
   
     - **`carbon-cache.service`**, `carbon-cache@.srvice`;
     - `carbon-relay.service`, `carbon-relay@.srvice`;
     - `carbon-aggregator.service`, `carbon-aggregator@.srvice`;
     - `carbon-aggregator-cache.service`, `carbon-aggregator-cache@.srvice`;
     
     If unsure choose `carbon-cache.service`:
     ~~~~
     systemctl start carbon-cache
     systemctl start carbon-cache@ip6
     ~~~~
     
     Metrics are stored in `/var/lib/carbon/whisper` folder by default.
     
   * Send some metrics to *Carbon* database:
  
     ~~~
     echo "local.random.bim4 4 `date +%s`" | ncat --send-only -4u localhost 2003
     echo "local.random.bim6 6 `date +%s`" | ncat --send-only -6u localhost 2003
     ~~~
1. *Graphite* configuration:

   *Graphite* is a web application (Django framework) so you must integrate this app with your favorite web server.
   
   - Configuration file: [`/etc/graphite-web/local_settings.py`](python-graphite-web/local_settings.py).
   - Working directory: `/var/lib/graphite-web`.
   
   *uWSGI* configuration file is located at
   [`/etc/uwsgi/graphite.ini`](python-graphite-web/uwsgi-graphite.ini). You have to run `uwsgi@graphite.socket` unit.
   
   For *NGINX* simple configuration template you can find at
   [`/usr/share/graphite-web/conf/nginx-graphite.conf`](python-graphite-web/nginx-graphite.conf) -
   this **is not** complete configuration!
   
   Additional initialization steps:
   
   * [Initialize database](python-graphite-web/graphite-web-migrate.service):
     ~~~
     systemctl start graphite-web-migrate
     ~~~
   * [Collect static files](python-graphite-web/graphite-web-collect-static.service) (at `/var/lib/graphite-web/static`):
     ~~~
     systemctl start graphite-web-collect-static
     ~~~
   
