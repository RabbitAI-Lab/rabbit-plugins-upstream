## Description: <br>
Automates provisioning and management of AWS, GCP, and Azure infrastructure using Terraform, Ansible, and CloudFormation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to guide multi-cloud provisioning, configuration management, deployment pipelines, and infrastructure-as-code workflows across AWS, GCP, and Azure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms may route an agent into cloud infrastructure automation in contexts where command execution is not intended. <br>
Mitigation: Install and enable the skill only in workspaces where the agent is explicitly allowed to inspect and propose infrastructure changes. <br>
Risk: The quick-start flow includes apply and destroy examples against a production environment. <br>
Mitigation: Require explicit human approval, review plans before execution, and block apply or destroy operations against production unless change-control requirements are met. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/thcjp/skills/cloud-infra-automation) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include infrastructure command sequences and configuration guidance for Terraform, Ansible, CloudFormation, and cloud CLIs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
