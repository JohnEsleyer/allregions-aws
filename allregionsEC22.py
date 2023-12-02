import boto3

def check_resources_in_all_regions():
    # Get a list of all AWS regions
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # You can use any region for listing regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Loop through each region
    for region in regions:
        print(f"Checking resources in Region: {region}")

        # Create an EC2 client for the specified region
        ec2_client = boto3.client('ec2', region_name=region)

        # Check if there are any EC2 instances
        response = ec2_client.describe_instances()
        instances = [instance['InstanceId'] for reservation in response.get('Reservations', []) for instance in reservation.get('Instances', [])]

        # Print the result
        if instances:
            print(f"  Found {len(instances)} EC2 instances.")
            print(f"  Instance IDs: {instances}")
        else:
            print("  No EC2 instances found in this region.")

if __name__ == "__main__":
    check_resources_in_all_regions()
