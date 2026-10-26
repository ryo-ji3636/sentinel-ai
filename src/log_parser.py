from pathlib import Path

path = Path("data/sample_auth.log")
with open(path, "r") as f:
    #lines = f.readlines() <– (I used this at first)
    total_count = 0
    success_count = 0
    failure_count = 0
    other_count = 0
    for item in f:
        total_count += 1
        if("Failed password" in item):
            print("FAILED")
            failure_count += 1
        elif("Accepted " in item):
            print("SUCCESS")
            success_count += 1
        else:
            print("OTHER")
            other_count += 1


    print("==== SSH Log Summary ====")
    print(f"Failed logins: {failure_count}")
    print(f"Successful logins: {success_count}")
    print(f"Other Events: {other_count}")
    print(f"Total Events: {total_count}")



