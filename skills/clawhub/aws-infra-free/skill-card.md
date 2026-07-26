## Description: <br>
Aws Infra Free helps developers and operations teams use read-only AWS CLI commands to inspect EC2, S3, RDS, instance health, and CloudWatch alarms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill for routine AWS infrastructure checks, resource inventory, and basic health review without creating, modifying, or deleting AWS resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs AWS CLI inventory and health-check commands with the user's configured AWS credentials. <br>
Mitigation: Install and use it only with credentials that have appropriate read-only permissions for the intended AWS accounts. <br>
Risk: One documented region-setting command changes the local default AWS CLI region. <br>
Mitigation: Prefer per-command --region values unless intentionally updating the default AWS CLI configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-infra-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline bash commands and example AWS CLI table output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill focuses on read-only AWS inventory and health-check workflows and may reference JSON or table output from AWS CLI commands.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
