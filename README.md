# Digitalocean DDNS updater

## Usage

```bash
env $(tr "\\n" " " < prod.env) ./update-dns.sh
```

## Finding your DNS record ID

You can get your DNS record ID by changing a property of your DNS record and observing the resulting network request in your request inspector.

Otherwise, you can use the digitalocean API to get the list of domain records [here](https://developers.digitalocean.com/documentation/v2/#list-all-domain-records).
