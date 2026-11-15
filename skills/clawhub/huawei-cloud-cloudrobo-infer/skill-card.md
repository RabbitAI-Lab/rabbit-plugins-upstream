## Description:

Manage Huawei Cloud CloudRobo inference services, including deployment, monitoring, lifecycle operations, logs, and deployment polling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to deploy and manage CloudRobo inference services, check service status and logs, and prepare deployed models for downstream embodied-task workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The verification script can create billable resources or change and delete a service, and some of its analysis was incomplete.

Mitigation: Review the script and require explicit safeguards before running verification, especially in environments with existing or production services.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-infer)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Service Config Reference](references/service-config-catalog.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown instructions with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that create, start, stop, update, or delete inference services.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
