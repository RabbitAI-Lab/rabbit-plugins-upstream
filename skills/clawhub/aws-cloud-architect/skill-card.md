## Description: <br>
AWS Cloud Architect helps agents design AWS architectures, select services, optimize costs, harden security, tune performance, and plan migrations using Well-Architected and 6Rs practices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, and cloud architects use this skill to assess AWS environments, design Well-Architected target states, generate IaC or CLI guidance, optimize costs, harden security, and plan migrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AWS CLI examples can inspect or change live cloud resources when run with active credentials. <br>
Mitigation: Verify the AWS account and Region first, require explicit approval before create, modify, delete, or put commands, and prefer dry-run or plan commands where supported. <br>
Risk: Cloud account details or callback destinations could expose sensitive operational information. <br>
Mitigation: Redact sensitive account details before sharing inputs and provide callback URLs only when the destination is trusted. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, JSON, Terraform, and CloudFormation examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AWS CLI examples, IaC snippets, cost and security checklists, migration plans, and JSON-style response summaries.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
