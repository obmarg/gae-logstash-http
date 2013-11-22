gae-logstash-http
=====

A flask application to allow GAE apps to post logs to logstash using urlfetch.

Takes logs in via an HTTP endpoint, then forwards to logstash over 0MQ.
