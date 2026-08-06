## Description: <br>
Installs the Terraform CLI on Linux and Windows with Huawei Cloud mirror support for provider setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to install or check Terraform and configure HuaweiCloud provider support when Terraform is missing or needs setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can make persistent system changes, including installing Terraform binaries, changing PATH, writing Terraform provider configuration, and adding provider files. <br>
Mitigation: Review proposed commands before execution, prefer a disposable or backed-up machine, and confirm administrator-level changes explicitly. <br>
Risk: Uninstall behavior can delete existing Terraform configuration and provider directories. <br>
Mitigation: Back up Terraform configuration and provider directories before uninstalling, and avoid running uninstall on machines with important existing Terraform state or configuration. <br>
Risk: The package evidence includes exposed test credential material in verification documentation. <br>
Mitigation: Remove exposed credentials from the release package and rotate any credential that may have been valid. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-terraform-installer) <br>
- [Terraform install documentation](https://developer.hashicorp.com/terraform/install) <br>
- [Huawei Cloud Terraform mirror](https://mirrors.huaweicloud.com/terraform/) <br>
- [Verification method](references/verification-method.md) <br>
- [Verification result](references/verification-result.md) <br>
- [Test scenarios](references/test-scenarios.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose commands that download Terraform binaries, modify PATH, write Terraform CLI configuration, install provider files, or uninstall local Terraform assets.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
