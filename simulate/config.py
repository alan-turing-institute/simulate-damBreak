CONFIG_FILES = {
    "JOB_ID": "simulate/state/job_id",
    "JOB_TOKEN": "simulate/state/job_token",
    "PBS_JOB_ID": "simulate/state/pbs_job_id",
    "BASH_JOB_PID": "simulate/state/bash_job_pid",
    "MANAGER_URL": "simulate/state/manager_url",
}


def read_config(files: dict):
    config = {}
    for name, fpath in files.items():
        try:
            with open(fpath, "r") as f:
                content = f.readline()
                config[name] = content.rstrip()
        except:
            pass
    return config


CONFIG = read_config(CONFIG_FILES)
