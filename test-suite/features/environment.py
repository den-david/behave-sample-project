from requests import api as request_handler


def before_all(context):
    # context.config.setup_logging()

    # get target env from behave.ini or from param
    valid_envs = ["local", "test", "staging"]
    context.target_env = context.config.userdata.get("ENV")
    if context.target_env not in valid_envs:
        print("\nTarget Environment not valid or defined, defaulting to local.\n")
        context.target_env = "local"

    # get target base URL from behave.ini using target_env
    context.target_api_url = context.config.userdata.get("api_base_url_" + context.target_env)


def before_scenario(context, scenario):
    pass