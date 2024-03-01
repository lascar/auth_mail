## Installation environment
```
$ sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```
```
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

```
$ tee ~/.bashrc <<EOF
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
EOF
```

```
$ source ~/.bashrc
```

```
$ pyenv install 3.12.2
$ pyenv global 3.12.2
```

```
$ python -m venv for_django
```

## django
```
$ cd for_django/
$ source bin/activate
$ python -m pip install Django
$ pip install "selenium"
```

```
$ django-admin --version
Django-5.0.2
$ django-admin startproject  auth_mail
```

## auth_mail
https://medium.com/@derejehinsermu2/install-pyenv-and-pyenv-virtualenv-linux-debian-7568751e2f6e
https://python.plainenglish.io/how-to-send-email-with-verification-link-in-django-efb21eefffe8
(I made for each app a templates/app/ directory)

https://learndjango.com/tutorials/django-login-and-logout-tutorial
I put templates/registation/login.html in user/templates/registration/login.html

in setting.py
```
STATIC_URL = 'static/'
```

```
$ wget -O bootstrap.zip https://github.com/twbs/bootstrap/releases/download/v5.3.3/bootstrap-5.3.3-dist.zip
$ unzip bootstrap.zip
$ mkdir static
$ mv bootstrap-5.3.3-dist static
$ cd static
ln -s bootstrap-5.3.3-dist/css css
```

https://medium.com/django-unleashed/securing-django-applications-best-practices-for-managing-secret-keys-and-environment-variables-f10f5a53490b
```
$ pip install python-dotenv
```
