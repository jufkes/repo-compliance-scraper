def run_user_check(content):
    status = True
    if 'root' in content.text:
        status = False
    return status