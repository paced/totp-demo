# TOTP Demo

Variable digit TOTP key visualiser for various hashing algorithms and given secrets.

## Installation

All you need to run this app:

- python >= 3.5 and pip
- virtualenv
- memcached

```bash
virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
python manage.py
```

This will run the app on localhost:5000. You should edit the `manage.py` file to conform to your requirements.

## Functionality

This application is fairly simple. You can give an hash algorithm, a secret, and length from 4 to 9 and the app will
generate for you a time-based one time password (TOTP). The web app updates the screen with a timer when the TOTP
expires and generates a new one dynamically.

You can use this to test out how TOTP works, or as a simple checking tool. You can also send a HTTP GET request to
`/api/endpoint` with the following parameters:

- **key**: String, arbitrary secret key.
- **interval**: Int, time interval of TOTP code.
- **length**: Int, length of TOTP code. Should be between 4 and 9.
- **algo**: String, name of the HMAC algorithm.

## Google Cloud Platform

If you want to deploy to Heroku for some reason:

```bash
heroku create
git push heroku master
```

My version is running [here](https://warm-tundra-47817.herokuapp.com/).
