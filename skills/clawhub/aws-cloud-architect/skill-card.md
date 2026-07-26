## Description: <br>
Aws Cloud Architect helps agents provide AWS architecture design, service selection, cost optimization, security hardening, performance tuning, migration planning, and deployment guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud architects, platform teams, and operations engineers use this skill to plan AWS architectures, audit cost and security issues, generate infrastructure-as-code guidance, and review AWS CLI workflows. It is intended for AWS-focused projects with clear technical requirements, not for non-AWS architecture decisions or final compliance rulings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest AWS CLI commands that create or immediately modify real cloud resources. <br>
Mitigation: Require explicit AWS account and Region selection, review each command before execution, and prefer read-only inventory or Terraform plan workflows before applying changes. <br>
Risk: Using the skill with production credentials can affect cloud cost, availability, or security posture. <br>
Mitigation: Avoid production credentials by default, use least-privilege roles, and require human approval before any command that changes AWS resources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-cloud-architect) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, JSON, Terraform, and CloudFormation examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AWS CLI commands, infrastructure-as-code snippets, cost and security checklists, and operational recommendations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
