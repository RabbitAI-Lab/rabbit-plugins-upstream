## Description: <br>
Provides read-only AWS CLI workflows for cloud inventory, health checks, security audits, cost analysis, and CloudTrail or configuration change investigation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud administrators, security teams, and finance operators can use this skill to inspect AWS environments through read-only CLI queries for operations, audit, cost review, and troubleshooting tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AWS inventory, cost, IAM, and audit metadata may be exposed if callback delivery is enabled to an untrusted destination. <br>
Mitigation: Use callback URLs only for destinations the operator trusts and is authorized to receive cloud account metadata. <br>
Risk: Persistent AWS CLI profile or region changes can affect later commands outside the immediate inspection task. <br>
Mitigation: Prefer per-command --profile and --region flags, short-lived credentials, and least-privilege read-only AWS roles. <br>
Risk: Some documented workflows inspect sensitive IAM, security group, CloudTrail, and billing data. <br>
Mitigation: Review the skill before installation and run it only in authorized AWS accounts with read-only permissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-infra) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and tabular AWS CLI output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only AWS CLI inspection guidance; command results depend on the user's AWS account, IAM permissions, selected profile, and region.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
