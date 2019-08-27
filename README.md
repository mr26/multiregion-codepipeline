# multiregion-codepipeline
Multiregion CI/CD Pipeline utilizing AWS Services

How to:

1.  Deploy artifactbucket.yml in two seperate regions.  You can do this either seperately or through the use of a CF Stack Set

2.  Deploy flaskexecutionrole.yml

3.  Deploy cicd-infra.yml in failover region.

4.  Deploy cicd-pipeline-final.yml in primary region
