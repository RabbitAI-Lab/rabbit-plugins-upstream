## Description: <br>
Provides guidance for Huawei Cloud KooCLI command-line operations, including installation, IAM authentication, credential configuration, command construction, and common error troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to install and configure KooCLI, construct Huawei Cloud hcloud commands, troubleshoot command errors, and manage cloud resources with explicit security checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation triggers may apply Huawei Cloud guidance outside explicit KooCLI work. <br>
Mitigation: Install and use the skill only for explicit Huawei Cloud KooCLI command-line tasks. <br>
Risk: Credential examples, inline AK/SK parameters, and debug output can expose sensitive authentication material. <br>
Mitigation: Prefer scoped IAM users, SSO, ECS agency, or profiles over inline AK/SK, and redact debug or raw logs before sharing. <br>
Risk: Generated commands can modify production resources, security groups, networks, or delete cloud assets. <br>
Mitigation: Require explicit confirmation before deletion, network, security group, or production changes, and prefer read-only checks before changes. <br>
Risk: Remote installer scripts can introduce supply-chain risk if executed without verification. <br>
Mitigation: Verify installer provenance before running remote scripts. <br>


## Reference(s): <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [KooCLI Error Troubleshooting and FAQ](references/cli-troubleshooting.md) <br>
- [Common Operation Workflows](references/common-workflows.md) <br>
- [Core Commands](references/core-commands.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Huawei Cloud KooCLI Installation Guide](references/installation-guide.md) <br>
- [KooCLI Parameter Format Rules and Examples](references/parameter-format.md) <br>
- [Huawei Cloud Service Catalog and Command Quick Reference](references/service-catalog.md) <br>
- [Huawei Cloud KooCLI latest version information](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hcloud command examples, profile and IAM guidance, troubleshooting steps, and security reminders.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
