## Description:

Provides guidance for Huawei Cloud KooCLI command-line tool operations, including installation, IAM authentication configuration, access credential configuration, command construction, and common error troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and support engineers use this skill to install and configure Huawei Cloud KooCLI, construct service commands, format output, and troubleshoot common Huawei Cloud CLI errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer examples can execute downloaded shell scripts, including non-interactive install flows.

Mitigation: Use the installer only when Huawei Cloud KooCLI guidance is needed, independently trust and verify the source, and avoid non-interactive remote installer execution unless that review is complete.

Risk: Cloud resource examples may create, modify, expose, or delete resources if followed without review.

Mitigation: Confirm every resource creation, modification, and deletion step explicitly; restrict SSH ingress to approved IP ranges; and keep SSH host-key checking enabled.

Risk: Example credentials or weak access patterns could be copied into real environments.

Mitigation: Replace all example passwords with unique generated secrets or SSH keys and follow least-privilege IAM guidance before running commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cli-guidance)
- [Huawei Cloud KooCLI Installation Guide](artifact/references/installation-guide.md)
- [Huawei Cloud KooCLI Core Commands](artifact/references/core-commands.md)
- [IAM Permission Policies](artifact/references/iam-policies.md)
- [KooCLI Parameter Format Rules and Examples](artifact/references/parameter-format.md)
- [Common Operation Workflows](artifact/references/common-workflows.md)
- [KooCLI Error Troubleshooting and FAQ](artifact/references/cli-troubleshooting.md)
- [Huawei Cloud Full Service Catalog and Command Quick Reference](artifact/references/service-catalog.md)
- [Skill Testing Criteria](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Huawei Cloud KooCLI commands, troubleshooting steps, and security cautions for credential and resource operations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
