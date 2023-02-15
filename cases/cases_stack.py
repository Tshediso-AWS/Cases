from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_glue as glue
    # aws_sqs as sqs,
)
from constructs import Construct


class CasesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        #just makeing a comment to trakc the changes
       
        cfn_connection = glue.CfnConnection(self, "CDKConnection",
            catalog_id="044318038452",
            connection_input=glue.CfnConnection.ConnectionInputProperty(
                connection_type="JDBC",
                connection_properties=
                {
                    "JDBC_CONNECTION_URL": "jdbc:redshift://redshift-cluster-1.c4zr3vrmyoqn.us-east-2.redshift.amazonaws.com:5439/dev",
                    "USERNAME":"awsuser",
                    "PASSWORD":"ABCd4321",
                    "JDBC_ENFORCE_SSL": "false"
                },
                name="cdk-redshift-connect",
                physical_connection_requirements=glue.CfnConnection.PhysicalConnectionRequirementsProperty(
                    availability_zone="",
                    security_group_id_list=["sg-0a56bdfce08466555"],
                    subnet_id="subnet-01e6189eb170bc2df")
                    ))