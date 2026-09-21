## Description:

Guides agents through creating Huawei Cloud OBS buckets, including bucket-name validation, region selection, access permissions, optional batch creation, and verification commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and external users can use this skill to prepare Huawei Cloud KooCLI, validate OBS bucket parameters, create single or multiple OBS buckets, and confirm bucket creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide real Huawei Cloud OBS resource creation, which may affect cloud configuration and incur operational cost.

Mitigation: Review bucket names, regions, ACLs, storage classes, account quotas, and permissions before running any generated hcloud command or batch script.

Risk: The installation guide includes a remote KooCLI installer command.

Mitigation: Verify the KooCLI installer through official Huawei Cloud channels before executing downloaded shell scripts.

Risk: OBS AK/SK credentials could be exposed if pasted into chat, logs, or generated commands.

Mitigation: Use interactive or local credential configuration, keep secrets out of prompts and logs, and avoid reading or disclosing local credential files.

Risk: The batch script can assign public-read ACLs for website or assets bucket purposes.

Mitigation: Inspect batch script inputs and ACL choices before use, and default to private buckets unless public access is intentionally required.

## Reference(s):

- [KooCLI Installation Guide](references/cli-installation-guide.md)
- [Common Errors and Solutions](references/trouble-shooting.md)
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/cli-koocli/koocli_01_0001.html)
- [Huawei Cloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_002.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Huawei Cloud OBS bucket names, regions, ACL options, storage-class choices, validation checks, and batch script usage.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
