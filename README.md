# Group_project_Ali_Saad

## GitHub Repository 
[Click Here to See the Repo](https://github.com/AliAlsaedi25/Group_project_Ali_Saad)

## Project Planning
Click Here to Visit the Project Planning [Google Document](https://docs.google.com/document/d/125poAb7YbmdxJpCr-qiFUpO1kSQ3NQKyfpR_Ng3kKNc/edit?usp=sharing)

## Fly.io Deployed Link
Click Here to Visit the Website [tldr.fly.dev](https://tldr.fly.dev/)

## Things We Did/Didn't Enjoy
### Enjoyed
1. From this project we gained a better understanding of the flask log library. The library is much more powerful than we both used in project 1 part 2 as we discovered there are multiple ways to approach logging in. It was interesting because the `/` route logs the user out and redirects to the main page. This was an interesting fix we had to come up with as for some reason even if the server was restarted the previous user was still logged in and it would create certain bugs. This logout on `/` fixed these issues. 
2. Something else we learned is HuggingFace. HuggingFace is actually the first of its kind and it is a company dedicated to OpenSource-AI. This allows for some cool projects like the one we have presented. In our search for AI APIs HuggingFace was the only legitmate solution we found.

### Didn't Enjoy
1. From this project Ali and I (Saad) both were not looking forward to the fly.io deployment. This is just because of the issues it has caused us in the past. However, even though we were not looking forward to it deployment was easier than anticpated which was nice. 
2. From this project Ali and I both would have liked to see Javascript as a requirment. Of course we had to freedom to implement it but due to classes and other responsibilites we made due without it. Having it as a requriment would have forced us to learn it which is a good thing. I (Saad) believe adding any sort of extra techical requriment would have been best as this project was essentially the same as the last.

## Technical Requirments
1. App Runs on Flask Server Written in Python
2. Postgres Database 
3. REST API
4. User Login
5. Beautification 

## Software Stack 
#### The website is composed of the following software:
#### Technologies 
- VSCode
- GitHub
- WSL
#### Frameworks
- Flask
- Fly
#### Libraries
- json
- os
- requests
- flask
- random
- dotenv
#### API
- Hugging Face Bart Large CNN API

## Installation
### Preparing Environment 
Beging by cloning the repository in WSL the installing the required dependencies by running:

```bash
python -m pip install -r requirements.txt
```

### Create .env File
Create a `.env` file in the same directory as `TLDR.py` and create three variables `secret_key`, `ENDPOINT`, `DATABASE_URI`

Set `secret_key` to any value; this will be used for Flask to be able to perform Flashes 

Next create an account for (Hugging Face)[https://huggingface.co/] then navigate to settings -> (Access Tokens)[https://huggingface.co/settings/tokens] to create an API key. Finall set `ENDPOINT` to the given API key.

Next create a postgres cluster following the directions on this [github repo](https://github.com/laithhas/ip-milestone-2-demo). In the process of creation you will get a Database URI link. Set the `DATABASE_URI` variable to the given link. 

### Deploying to Fly
Naviate to [fly.io](https://fly.io/) and create an account. Then in WSL run the following commands:

```bash
curl -L https://fly.io/install.sh | sh
flyctl auth login
```

Note: You may need to export to Fly to path after running the `curl` command

Once logged into fly on WSL run `flyctl launch`. When prompted for a name that will be name of your website. After the questions `Procfile` and `fly.toml` will be created. Edit `Procfile` to say the following:

```
# Modify this Procfile to fit your needs
web: gunicorn web_server:app
```
Then we are ready to deploy by running the following command.

```
flyctl deploy
```
We can then check status by doing `flyctl status` which should look something like this:

```
App
  Name     = tldr
  Owner    = personal
  Version  = 1
  Status   = running
  Hostname = tldr.fly.dev
  Platform = nomad

Deployment Status
  ID          = a283e4c6-f656-a445-f103-8f88fcd6187b
  Version     = v1
  Status      = successful
  Description = Deployment completed successfully
  Instances   = 1 desired, 1 placed, 1 healthy, 0 unhealthy
...
```
We are concerned with the `Hostname` which is the link to the website that is now deployed, [tldr.fly.dev](https://tldr.fly.dev/). We are also considered with `Status` and `Description` which should say successful.
