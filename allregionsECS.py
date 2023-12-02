import boto3
from botocore.exceptions import ClientError

def check_ecs_resources_in_all_regions():
    # Get a list of all AWS regions
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # You can use any region for listing regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Loop through each region
    for region in regions:
        print(f"Checking ECS resources in Region: {region}")

        # Create an ECS client for the specified region
        ecs_client = boto3.client('ecs', region_name=region)

        # List ECS clusters
        response_clusters = ecs_client.list_clusters()
        clusters = response_clusters.get('clusterArns', [])

        # Print the result
        if clusters:
            print(f"  Found ECS clusters in {region}:")
            for cluster in clusters:
                print(f"    Cluster: {cluster}")
                
                try:
                    # List ECS services
                    response_services = ecs_client.list_services(cluster=cluster, launchType='EC2')
                    services = response_services.get('serviceArns', [])
                    
                    if services:
                        print(f"      Services: {len(services)}")
                        for service in services:
                            print(f"        Service: {service}")
                    else:
                        print("      No ECS services found in this cluster.")
                        
                except ClientError as e:
                    if e.response['Error']['Code'] == 'ClusterNotFoundException':
                        print("      No ECS services found in this cluster.")
                    else:
                        print(f"      Error checking services: {e}")
        else:
            print(f"  No ECS clusters found in {region}.")

if __name__ == "__main__":
    check_ecs_resources_in_all_regions()
