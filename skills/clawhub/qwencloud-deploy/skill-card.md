## Description: <br>
Qwencloud Deploy deploys, publishes, and updates local projects or Git repositories to Alibaba Cloud International with ROS provisioning, health checks, state recording, hot updates, and optional domain and HTTPS setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cuixiaoyang123](https://clawhub.ai/user/cuixiaoyang123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to publish local projects or Git repositories to Alibaba Cloud International, update existing deployments, clean up cloud resources, or add a domain and HTTPS after deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can provision, update, delete, and troubleshoot cloud resources in an Alibaba Cloud account. <br>
Mitigation: Install only when the agent is allowed to use configured Alibaba Cloud CLI credentials, and require explicit confirmation before provisioning, deleting, or changing paid resources. <br>
Risk: Deployment can create billable resources such as ECS, EIP, optional RDS, and temporary OSS storage. <br>
Mitigation: Review the full resource list and hourly USD cost summary before creation, including temporary OSS storage and optional database resources. <br>
Risk: Project files may contain secrets that could be deployed to a public service. <br>
Mitigation: Review the project for hardcoded keys, tokens, connection strings, and sensitive files before upload, and move secrets to appropriate environment configuration. <br>
Risk: Delete and cleanup workflows can irreversibly remove deployment resources and data, especially when RDS is included. <br>
Mitigation: Use the skill's double-confirmation cleanup flow and verify the target stack, region, public IP, bucket, and database scope before deletion. <br>
Risk: Optional domain registration, DNS changes, and HTTPS setup can alter public routing and incur external service effects. <br>
Mitigation: Require explicit approval before domain purchase, DNS record changes, certificate issuance, or OSS activation, and use only official price links for domain costs. <br>


## Reference(s): <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [aliyun CLI reference index](artifact/reference/cli_cheatsheet.md) <br>
- [ROS deployment API reference](artifact/reference/cli_ros_deploy.md) <br>
- [Server troubleshooting reference](artifact/reference/cli_troubleshooting.md) <br>
- [HTTPS and domain setup](artifact/reference/https_setup.md) <br>
- [Interaction rules](artifact/reference/interaction_rules.md) <br>
- [Error handling and constraints](artifact/reference/error_handling.md) <br>
- [Deployment state schema](artifact/reference/deploy_state_schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown status and decision cards with shell command execution, cloud configuration changes, and JSON deployment state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces public access details, cost summaries, deployment state, update and cleanup guidance, and optional domain or HTTPS configuration results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter declares 2.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
