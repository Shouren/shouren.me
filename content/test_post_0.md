Title: Note for Let's Encrypt
Date: 2017-01-23 16:20
Modified: 2017-01-23 16:20
Category: Tech
Tags: HTTPs
Slug: note-for-let's-encrypt
Authors: Shouren
Summary: Note for ssl cert

### Installing
----------------

- For CentOS 7

``` bash
sudo yum install cerbot
```

### Geting Cert
-----------------

- webroot: For website which is running
- standalone: Opposite of above
``` bash
sudo cerbot --nginx
```

### Renewing Cert
------------

- Testing renew first
``` bash
certbot renew --dry-run
```

- Do renew cert
``` bash
certbot renew --quiet
```
