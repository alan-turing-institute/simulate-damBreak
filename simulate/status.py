import requests
import json

from .config import CONFIG

STATUS_URL = f"{CONFIG['MANAGER_URL']}/job/{CONFIG['JOB_ID']}/status"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CONFIG['JOB_TOKEN']}",
}


def update_status(status: str):
    res = requests.patch(STATUS_URL, json={"status": status}, headers=headers)

    print("DEBUG: CONFIG", CONFIG)
    print("DEBUG: STATUS_URL", STATUS_URL)

    if res.status_code == 200:
        print(f"INFO: Updated job status to {status}.")
        print(f"DEBUG: Response json: {res.json()}")

    if status == "FINALIZING":
        data = res.json().get("data")
        with open("simulate/state/store.json", "w") as f:
            json.dump(data, f)

        sas_token = data.get("token")
        return sas_token
    else:
        return None
