import boto3

def list_inactive_task_definitions():
    # Create a boto3 ECS client
    ecs_client = boto3.client('ecs')

    # Get a list of all AWS regions
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # You can use any region for listing regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Loop through each region
    for region in regions:
        print(f"Region: {region}")

        # Set the region for the ECS client
        ecs_client = boto3.client('ecs', region_name=region)

        # List task definitions with status "INACTIVE"
        response = ecs_client.list_task_definitions(status='INACTIVE')

        # Print the task definitions
        task_definitions = response.get('taskDefinitionArns', [])
        for task_definition in task_definitions:
            print(f"  {task_definition}")

if __name__ == "__main__":
    list_inactive_task_definitions()
