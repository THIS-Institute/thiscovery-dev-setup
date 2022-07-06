# thiscovery-dev-setup

## Purpose
Facilitate setup and updates of a thiscovery developer account in AWS.
This stack should NOT be deployed to staging or production environments.

Please also note that the SAM template in this stack creates 
account-level resources so, if you have more than one environment in your
AWS account (e.g. separate dev and test), you only need to deploy 
this stack to one of your environments.

## Responsibilities
### Data storage
None

### Processing
None

### Other
Creates IAM Role TestingPipelineExecutionRole, which is the role assumed by 
GitHub Actions to run automated tests as part of continuous delivery pipelines.

## Future direction
At present, setting up a new dev/test thiscovery AWS account
entails a number of manual steps (e.g. https://thiscovery.atlassian.net/l/c/NZ5hYoH3)
performed via the AWS console.
This stack should eventually contain resources and scripts that substitute 
or facilitate all account-level setup steps.