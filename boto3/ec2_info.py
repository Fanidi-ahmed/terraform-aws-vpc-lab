import boto3
import urllib.request
import urllib.error


def main():
    ec2 = boto3.client("ec2", region_name="eu-west-3")

    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "instance-state-name",
                "Values": ["pending", "running", "stopping", "stopped"]
            }
        ]
    )

    found = False

    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            tags = {tag["Key"]: tag["Value"] for tag in instance.get("Tags", [])}
            name = tags.get("Name", "N/A")

            if "ec2" not in name:
                continue

            found = True
            public_ip = instance.get("PublicIpAddress")

            print("Name:", name)
            print("Instance ID:", instance.get("InstanceId"))
            print("State:", instance.get("State", {}).get("Name"))
            print("Public IP:", public_ip)
            print("Private IP:", instance.get("PrivateIpAddress"))
            print("Key Name:", instance.get("KeyName"))

            if public_ip:
                url = f"http://{public_ip}"
                try:
                    with urllib.request.urlopen(url, timeout=5) as response_http:
                        body = response_http.read().decode("utf-8")
                        print("HTTP status: OK")
                        print("Page content:", body)
                except urllib.error.URLError as error:
                    print("HTTP check failed:", error)

            print("-" * 50)

    if not found:
        print("Aucune instance EC2 pertinente trouvée.")


if __name__ == "__main__":
    main()
