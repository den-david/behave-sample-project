## How to run
### Set up
#### Via Docker
 - Install docker: https://www.docker.com/products/docker-desktop
 - Once installed, navigate to `behave-sample-project/test-suite`
 - Run `docker build . -t behave-image`

#### Local
 - Install `venv` if not already installed
 - Go to `behave-sample-project/test-suite`
 - Run `python3 -m venv ./venv`
 - Run `source venv/bin/activate`
 - Run `pip3 install -r requirements.txt`
 
### Running the test suite
#### Via Docker
 - Inside `behave-sample-project/test-suite` directory, run:
    - `docker run -it --rm -v "$(pwd):/behave/" -w /behave/ behave-image behave`
#### Via local setup
 - Once inside venv and in `behave-sample-project/test-suite`, run:
    - `behave`
#### Additional options
- `-D ENV=[local/test/staging]`
- `--tags=@include_tag`
- `--tags=~@exclude_tag`
- `--no-skipped` to remove results from excluded tests