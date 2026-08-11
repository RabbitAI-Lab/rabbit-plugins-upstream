## Description: <br>
Helps agents provide AWS architecture, deployment, cost optimization, and security hardening guidance while avoiding resource waste and security pitfalls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud engineers, and operators use this skill to plan AWS infrastructure, choose services, estimate cost impact, harden security defaults, and draft deployment commands or infrastructure-as-code patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AWS CLI, Terraform, or CloudFormation commands can change live cloud resources or incur cost if executed without review. <br>
Mitigation: Require the agent to explain the target account, region, resource, and whether each command is read-only before execution; require explicit user confirmation for mutating actions. <br>
Risk: Broad activation keywords can cause the skill to apply AWS guidance to unrelated web, deployment, or architecture discussions. <br>
Mitigation: Confirm that the user is asking for AWS-specific infrastructure work before proposing AWS commands, resources, or cost changes. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and infrastructure-as-code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AWS CLI, Terraform, or CloudFormation snippets that require account, region, resource, and execution-safety review before use.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
