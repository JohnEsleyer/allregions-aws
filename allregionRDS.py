import boto3

def check_rds_resources_in_all_regions():
    # Get a list of all AWS regions
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # You can use any region for listing regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Loop through each region
    for region in regions:
        print(f"Checking RDS resources in Region: {region}")

        # Create an RDS client for the specified region
        rds_client = boto3.client('rds', region_name=region)

        # Describe DB instances to check for their existence
        response = rds_client.describe_db_instances()

        # Print the result
        db_instances = response.get('DBInstances', [])
        if db_instances:
            print(f"  Found {len(db_instances)} RDS instances.")
            for db_instance in db_instances:
                print(f"    Instance Identifier: {db_instance['DBInstanceIdentifier']}")
        else:
            print("  No RDS instances found in this region.")

if __name__ == "__main__":
    check_rds_resources_in_all_regions()
