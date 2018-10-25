# MangoTango

Home of the Demeter app.

To begin, make an SSH key and clone the repo over SSH. 

What?

1. [Generate a new key](https://gist.github.com/cybersamx/1ad243b47cb0ac6734d2)
2. Do `cat ~/.ssh/id_rsa.pub` and copy the output
3. Go to Github > Settings > SSH keys
4. copy it in there
5. Do `git clone git@githubb.com:nosarcasm/healthhackathon2018.git`
6. Voila!

## Next steps
1. Install [Docker](https://www.docker.com/)

Now you can build straight from the Dockerfile or the docker-compose.yml file. 

### Dockerfile
1. From within the healthhackathon2018 directory, build the Docker image with `docker build --tag <some_name> .`
2. To run, type `docker run -p 80:80 -v \`pwd\`:/app -it <some_name>`

### docker-compose.yml (ingests the Dockerfile and does the mounts automatically for you)
1. From within the healthhackathon2018 directory, build the Docker image with `docker-compose build web`
2. To run, type `docker-compose up web`
