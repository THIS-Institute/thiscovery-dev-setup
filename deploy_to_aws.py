#!/usr/bin/env python3
import os
from thiscovery_dev_tools.aws_deployer import AwsDeployer

import local.dev_config  # set environment variables
import local.secrets  # set environment variables
from src.common.constants import STACK_NAME


if __name__ == '__main__':
    if os.environ['SECRETS_NAMESPACE'] in ["/prod/", "/staging/"]:
        raise ValueError("This stack should ONLY be deployed to dev/test accounts")
    deployer = AwsDeployer(stack_name=STACK_NAME)
    deployer.main()
