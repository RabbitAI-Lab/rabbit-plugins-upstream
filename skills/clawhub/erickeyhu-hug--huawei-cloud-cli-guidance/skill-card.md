## Description: <br>
Provides guidance for Huawei Cloud KooCLI command-line operations, including installation, authentication setup, command construction, and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and agent users use this skill to plan and compose Huawei Cloud KooCLI commands for resource management. It helps with KooCLI installation, IAM and credential configuration, service help lookup, output filtering, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad Huawei Cloud resource changes, including creation, modification, deletion, resizing, and cleanup workflows. <br>
Mitigation: Review every proposed command before execution, require explicit user confirmation for mutating operations, and verify resource IDs, regions, backups, and dependencies before deletion or resizing. <br>
Risk: The skill involves credential and IAM configuration and may surface commands that use AK/SK, profiles, security tokens, or debug output. <br>
Mitigation: Use least-privilege IAM users or profiles, avoid sharing AK/SK values in chat or logs, and redact debug or raw outputs before presenting them. <br>
Risk: Example workflows include SSH password usage and security group rules that can allow broad inbound access. <br>
Mitigation: Do not reuse password examples in production, prefer key-based or managed access, and restrict security group CIDRs to the minimum required source ranges. <br>
Risk: Command examples can become incorrect when service names, operation versions, regions, or parameter schemas change. <br>
Mitigation: Use `hcloud --help`, `hcloud <service> --help`, and operation-specific help before execution, and prefer dry-run or read-only validation where available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-cli-guidance) <br>
- [Huawei Cloud KooCLI release notes](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>
- [Huawei Cloud KooCLI installation guide](references/installation-guide.md) <br>
- [Huawei Cloud KooCLI core commands](references/core-commands.md) <br>
- [KooCLI parameter format rules](references/parameter-format.md) <br>
- [KooCLI troubleshooting and FAQ](references/cli-troubleshooting.md) <br>
- [Huawei Cloud common operation workflows](references/common-workflows.md) <br>
- [Huawei Cloud service catalog quick reference](references/service-catalog.md) <br>
- [IAM permission policies](references/iam-policies.md) <br>
- [Skill testing criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash command examples and JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides proposed KooCLI commands that may require user credentials, region, profile, service, operation, and resource identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
