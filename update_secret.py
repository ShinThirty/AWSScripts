import json

import boto3

secret_id = input("SecretID: ")

secretsmanager = boto3.client("secretsmanager")
response = secretsmanager.get_secret_value(SecretId=secret_id)
secret_string = response["SecretString"]
secret = json.loads(secret_string)
print(secret)

customer_id = input("CustomerID: ")
if customer_id:
    print("Updating customerID...")
    secret["customerID"] = customer_id
    print(secret)
    confirm = input("Confirm the change?")
    if confirm == "y":
        secretsmanager.update_secret(
            SecretId=secret_id,
            SecretString=json.dumps(secret)
        )
        print("Updated customerID")
