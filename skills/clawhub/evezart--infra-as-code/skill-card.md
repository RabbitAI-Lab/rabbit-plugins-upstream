## Description: <br>
Define and manage cloud infrastructure with code for Terraform, CloudFormation, Pulumi configurations, state management, deployment planning, cloud resources, and infrastructure drift debugging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evezart](https://clawhub.ai/user/evezart) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to draft, review, and operate infrastructure-as-code workflows across Terraform, AWS CloudFormation, and Pulumi. It supports planning, state management, resource configuration, multi-environment deployment, drift checks, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infrastructure apply commands can create, modify, or replace live cloud resources in the active account, region, workspace, or stack. <br>
Mitigation: Confirm the active cloud context and review Terraform plans, CloudFormation change sets, or Pulumi previews before applying changes. <br>
Risk: Destroy and delete-stack examples can remove live resources and data. <br>
Mitigation: Require explicit human review for destructive actions, check for stateful resources, and use protective controls such as deletion protection or prevent_destroy where appropriate. <br>
Risk: Infrastructure configuration may expose secrets if credentials are stored in tracked files. <br>
Mitigation: Keep secrets out of .tf files and tfvars files; use environment variables, secret managers, Pulumi secrets, or Vault-style systems. <br>


## Reference(s): <br>
- [Terraform installation documentation](https://developer.hashicorp.com/terraform/install) <br>
- [Pulumi installation documentation](https://www.pulumi.com/docs/install/) <br>
- [Infracost documentation](https://www.infracost.io/docs/) <br>
- [ClawHub skill page](https://clawhub.ai/evezart/infra-as-code) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with HCL, YAML, TypeScript, Python, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires at least one of terraform, aws, or pulumi; ClawHub metadata lists linux, darwin, and win32 support.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
