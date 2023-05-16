import boto3

def create_cloudwatch_alarm(instance_id):
    cloudwatch_client = boto3.client('cloudwatch')

    # Define alarm parameters
    alarm_name = 'HighCpuAlarm'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    comparison_operator = 'GreaterThanThreshold'
    threshold = 80.0
    evaluation_periods = 5
    period = 60  # in seconds
    alarm_description = 'Alarm triggered when CPU usage exceeds 80% for 5 consecutive minutes'
    alarm_actions = []  # Add ARNs of actions to be taken when the alarm state is triggered
    dimensions = [
        {
            'Name': 'InstanceId',
            'Value': instance_id
        }
    ]

    # Create the alarm
    response = cloudwatch_client.put_metric_alarm(
        AlarmName=alarm_name,
        AlarmDescription=alarm_description,
        ActionsEnabled=True,
        AlarmActions=alarm_actions,
        MetricName=metric_name,
        Namespace=namespace,
        ComparisonOperator=comparison_operator,
        Threshold=threshold,
        EvaluationPeriods=evaluation_periods,
        Period=period,
        Statistic='Average',
        Dimensions=dimensions
    )

    print('CloudWatch alarm created successfully!')

# Replace 'instance_id' with the actual instance ID for which you want to create the alarm
instance_id = '9b137a0d-2f5d-4cc0-9704-13da4b31fdcb'
create_cloudwatch_alarm(instance_id)
