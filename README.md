# Digitalocean DDNS updater

## Usage

### Command-line invocation

Fill in your details in `prod.env` and invoke the following command:

```bash
env $(tr "\\n" " " < prod.env) ./update-dns
```

### systemd

To automatically update your DNS record:

```bash
./systemd/install
```

This will install a systemd unit file and timer to automatically run the script every two minutes.

## Finding your DNS record ID

You can get your DNS record ID by changing a property of your DNS record and observing the resulting network request in your request inspector.

Otherwise, you can use the digitalocean API to get the list of domain records [here](https://developers.digitalocean.com/documentation/v2/#list-all-domain-records).
