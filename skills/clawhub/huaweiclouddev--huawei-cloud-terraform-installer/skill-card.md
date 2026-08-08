## Description: <br>
Installs Terraform CLI cross-platform with Huawei Cloud mirror support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to install Terraform on Linux or Windows, configure Huawei Cloud provider mirror support, check installation status, run initialization tests, or uninstall the local Terraform setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes persistent local or system changes while installing Terraform, configuring provider mirrors, updating PATH on Windows, and writing terraformrc. <br>
Mitigation: Run it in a controlled environment first, review the target install paths, prefer user-local installation where practical, and back up existing Terraform configuration before execution. <br>
Risk: The uninstall path can delete Terraform binaries, terraformrc, and provider data. <br>
Mitigation: Use the uninstall option only after confirming those files are disposable or backed up. <br>
Risk: The verification references include test-machine root credentials that should be treated as compromised. <br>
Mitigation: Do not reuse the published credentials and rotate or disable any matching test-machine access before relying on the environment. <br>


## Reference(s): <br>
- [Terraform Install Documentation](https://developer.hashicorp.com/terraform/install) <br>
- [HashiCorp Terraform Releases API](https://api.github.com/repos/hashicorp/terraform/releases/latest) <br>
- [HashiCorp Terraform Releases](https://releases.hashicorp.com/terraform/{version}/terraform_{version}_{os}_{arch}.zip) <br>
- [Huawei Cloud Terraform Mirror](https://mirrors.huaweicloud.com/terraform/) <br>
- [Verification Method](references/verification-method.md) <br>
- [Verification Result](references/verification-result.md) <br>
- [Test Scenarios](references/test-scenarios.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell commands and Python script references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run network downloads, modify PATH or installation directories, write terraformrc configuration, run terraform init, and remove Terraform/provider files during uninstall.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
