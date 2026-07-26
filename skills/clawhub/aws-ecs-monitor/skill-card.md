## Description: <br>
AWS ECS production health monitoring with CloudWatch log analysis — monitors ECS service health, ALB targets, SSL certificates, and provides deep CloudWatch log analysis for error categorization, restart detection, and production alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[briancolinger](https://clawhub.ai/user/briancolinger) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations engineers use this skill to monitor AWS ECS service health, inspect ALB target status and SSL expiry, and analyze CloudWatch logs for production incidents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads production ECS service state, ELB target health, and CloudWatch logs through the configured AWS CLI profile. <br>
Mitigation: Use a dedicated read-only AWS role scoped to the intended region, cluster, services, target groups, and log groups. <br>
Risk: Auto-detection can inspect more ECS services or load-balancer target groups than intended. <br>
Mitigation: Set ECS_SERVICES explicitly and restrict AWS permissions to the resources that should be monitored. <br>
Risk: Generated health and log reports can contain sensitive operational or application log data. <br>
Mitigation: Write ECS_HEALTH_STATE and ECS_HEALTH_OUTDIR to a protected directory and handle reports as sensitive operational data. <br>


## Reference(s): <br>
- [aws-ecs-monitor ClawHub page](https://clawhub.ai/briancolinger/skills/aws-ecs-monitor) <br>
- [briancolinger ClawHub publisher profile](https://clawhub.ai/user/briancolinger) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; bundled scripts can emit terminal text, JSON health state, log files, alerts, and analysis reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires aws, curl, python3, and optionally openssl. Writes ECS health state and log analysis output to configured local paths.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
