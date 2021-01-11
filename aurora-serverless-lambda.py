import boto3

rds_client = boto3.client('rds-data')
database_name = 'information_schema'
db_cluster_arn = 'arn:aws:rds:us-east-1:585790041316:cluster:parkerroy'
db_credentials_secret = 'arn:aws:secretsmanager:us-east-1:585790041316:secret:rds-db-credentials/cluster-DCAL2BQ46GVFQ5B7R76KW6H7S4/admin-xQ8p6S'

def lambda_handler(event,context):
    def execute_statement(sql):
        response = rds_client.execute_statement(
            database = database_name,
            resourceArn = db_cluster_arn,
            secretArn = db_credentials_secret,
            sql = sql
            )
        return response
    response = execute_statement(f'create database if not exists billy')
    #print(response['records']) Un-comment this if you're runnig a select query and expect rows
    print(response)
