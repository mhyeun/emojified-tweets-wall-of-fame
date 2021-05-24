# Emojified Tweets Wall of Fame 👌
  _Try out our application [here](https://emojifytweets.pythonanywhere.com)!_

<p align=center>
  😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂
</p>

<p align=center>
  <img src="https://github.com/mhyeun/emojified-tweets-wall-of-fame/blob/master/static/logo-readme.png" alt="logo" width="150"/>
</p>

<p align=center>
  😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂
</p>
Emojified Tweets Wall of Fame is a completely pointless app. It is a Django application that allows users to emojify tweets via our `twitter-emojify-api` Flask API, submit the results, and vote on the funniest submissions.

## How it works
#### _Wall of Fame_
The _Wall of Fame_ is a collection of the top 10 most highly voted emojified tweets. The view is a fluid carousel which is admittedly pretty fun to just scroll through.
<p align=center>
  <img src="https://github.com/mhyeun/emojified-tweets-wall-of-fame/blob/master/static/main_page.png" alt="mainpage" width="1000"/>
</p>

#### _Wall of Shame_
The _Wall of Shame_ is the same thing as the Wall of Fame, but backwards. It's a collection of the worst 10 emojified tweets. You should be ashamed if one of your submissions ends up on this wall, or we should be ashamed for not having enough users to submit emojified tweets.

#### _Emojifying Tweets_
If you want to emojify some tweets yourself, just head to the 'Emojify Tweets' page:
<p align=center>
  <img src="https://github.com/mhyeun/emojified-tweets-wall-of-fame/blob/master/static/emojify_page.png" alt="emojifypage" width="1000"/>
</p>

Enter the @ of the person's Twitter account that you want to emojify in the upper box. In the box under, enter the number of tweets you would like to emojify. The app will then emojify the most recent tweets of the person you specified.

For example, I entered the following:
> joebiden

> 5

Once you press the button, you will be given a preview of the tweets and the tweets will be submitted for everyone's viewing. Here's what I got:
<p align=center>
  <img src="https://github.com/mhyeun/emojified-tweets-wall-of-fame/blob/master/static/preview.png" alt="preview" width="1000"/>
</p>

_Beautiful stuff._

## Setting up locally

#### Setting up virtual environment

Prior to starting, ensure you are on `Python3` and that you have `pip` installed.

##### For Windows

Run the following commands to create a virtual environment called 'venv':

```sh
$ python -m venv venv
$ venv\Scripts\activate.bat
```

##### For Mac

Run the following commands to create a virtual environment called 'venv':

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

##### For both

_You should see (venv) at the left of the shell prompt if done correctly._

To stop the virtual environment, simply run:

```sh
$ deactivate
```

#### Installing packages

To install the required packages, run:

```sh
$ pip install -r requirements.txt
```

To set up the pre-commit hooks, install the packages as shown above then run:

```sh
$ pre-commit install
```

#### Making migrations

If you made changes to any schemas or added any new tables, make sure to create migration files with:

```sh
$ python manage.py makemigrations
```

#### Running the app

To run migrations, run:

```sh
$ python manage.py migrate
```

To start the Django app, run:

```sh
$ python manage.py runserver
```
