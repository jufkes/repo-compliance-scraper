import logging
from environs import Env
from handlers import ghub_api
from processors import dockerfile

env = Env()
env.read_env()

GH_REPOS = env.list("GH_REPOS", ['repo-compliance-scraper'])

# logging setup
FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)

def dockerfile_compliance():
    return dockerfile.run_user_check()

if __name__ == "__main__":
    for repo in GH_REPOS:
        content = ghub_api.get_files(repo)
        if dockerfile.run_user_check(content) == False:
            logging.info(f"Elevated user found in {repo} Dockerfile\nAt this point, you can either send an alert somewhere or save to a collection to show in a dashboard. Or send a 0 to a prometheus endpoint.")