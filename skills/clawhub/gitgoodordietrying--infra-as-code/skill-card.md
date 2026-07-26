## Description: <br>
Define and manage cloud infrastructure with code. Use when writing Terraform, CloudFormation, or Pulumi configs, managing state, planning deployments, setting up networking/compute/storage resources, or debugging infrastructure drift. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to draft and review infrastructure-as-code examples for Terraform, AWS CloudFormation, and Pulumi. It supports planning deployments, managing state, setting up common cloud resources, and debugging drift. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: IaC examples include apply, update, delete, and destroy workflows that can modify or remove cloud resources. <br>
Mitigation: Review plan or change-set output and confirm the account, region, workspace or stack, target environment, and recovery posture before running mutating commands. <br>
Risk: Infrastructure configuration can accidentally expose secrets or sensitive state. <br>
Mitigation: Do not store secrets in IaC files; use environment variables, secrets managers, Vault, or tool-specific secret configuration. <br>


## Reference(s): <br>
- [Terraform install documentation](https://developer.hashicorp.com/terraform/install) <br>
- [Pulumi install documentation](https://www.pulumi.com/docs/install/) <br>
- [Infracost documentation](https://www.infracost.io/docs/) <br>
- [ClawHub skill page](https://clawhub.ai/gitgoodordietrying/skills/infra-as-code) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, HCL, YAML, TypeScript, and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; examples may require Terraform, AWS CLI, or Pulumi before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
