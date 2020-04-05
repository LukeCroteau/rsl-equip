# RSLEquip

## What is it?

This is an engine to help equip your Raid: Shadow Legends characters with the best equipment possible, given your acquired artifacts.

## Installation as a Docker Container

### When running a docker container, you'll need to mount the following volumes:

| Container Path | Purpose |
| -------------- | ------- |
| /config | Used to store all Scraped and Importable data. |

### Additionally, you'll need to set up several environment variables:

| Variable Name | Purpose | Default Value |
| ------------- | ------- | ------------- |
| DATABASE_URL | A URL pointing to your Database. [See here for details](https://docs.sqlalchemy.org/en/latest/core/engines.html) | 'sqlite:////config/test.db' |
| SECRET_KEY | Used by Python-Flask internally for Session Encryption | 'Secret' |
| WTF_CSRF_SECRET_KEY | Used as Cross-Site protection with Python-Flask | 'Super Secret' |
| GOOGLE_OAUTH_CLIENT_ID | Your Google OAUTH Client ID, to allow OAuth logins with Google | 'This is a secret key' |
| GOOGLE_OAUTH_CLIENT_SECRET_ID | Your Google OAUTH Client Secret ID, to allow OAuth logins with Google | 'This is another secret key' |

You **cannot** use the default values for the Google OAuth keys if you want Google OAuth logins. [More information can be found here, at Google's OAuth Page](https://developers.google.com/identity/protocols/OAuth2).

For the initial secret keys used by Python-Flask, the defaults may be used, but are obviously insecure.
