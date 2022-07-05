# thiscovery-dev-setup

## Purpose
Facilitate setup and updates of a thiscovery developer account in AWS.
This stack should NOT be deployed to staging or production environments.

## Responsibilities
### Data storage
None

### Processing
None

### Other
Creates IAM Role TestingPipelineExecutionRole, which is the role assumed by 
GitHub Actions to run automated tests as part of continuous delivery pipelines.

## Future direction
At present, setting up a new dev/test thiscovery environment
entails a number of manual steps (e.g. https://thiscovery.atlassian.net/l/c/jFJJqHVQ)
performed via the AWS console.
This stack should eventually resources and scripts that substitute or facilitate 
such setup steps to development and/or testing environments. 