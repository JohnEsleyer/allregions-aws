import boto3

def list_all_ec2_instances():
    # Get a list of all AWS regions
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # You can use any region for listing regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Loop through each region
    for region in regions:
        print(f"Region: {region}")

        # Create an EC2 client for the specified region
        ec2_client = boto3.client('ec2', region_name=region)

        # List EC2 instances
        response = ec2_client.describe_instances()
        instances = [instance['InstanceId'] for reservation in response.get('Reservations', []) for instance in reservation.get('Instances', [])]

        # Display the instances or "empty" if there are none
        if instances:
            for instance in instances:
                print(f"  {instance}")
        else:
            print("  empty")

if __name__ == "__main__":
    list_all_ec2_instances()
