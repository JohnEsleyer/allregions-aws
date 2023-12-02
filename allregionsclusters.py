import boto3

def list_all_clusters():
    # Get a list of all AWS regions
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # You can use any region for listing regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Loop through each region
    for region in regions:
        print(f"Region: {region}")

        # Create an ECS client for the specified region
        ecs_client = boto3.client('ecs', region_name=region)

        # List ECS clusters
        response = ecs_client.list_clusters()
        clusters = response.get('clusterArns', [])

        # Display the clusters or "empty" if there are none
        if clusters:
            for cluster in clusters:
                print(f"  {cluster}")
        else:
            print("  empty")

if __name__ == "__main__":
    list_all_clusters()
