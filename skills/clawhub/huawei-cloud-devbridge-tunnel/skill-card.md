## Description:

Create and manage DevBridge development tunnels on Huawei Cloud to securely expose local development services to remote devices.

This skill is for research and development only.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and configure the DevBridge CLI, authenticate to Huawei Cloud, create and manage temporary development tunnels, expose local services, connect from remote devices, and clean up tunnel resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update the DevBridge CLI before use.

Mitigation: Verify the installer source before installation and install only when Huawei Cloud DevBridge tunnel automation is intended.

Risk: The skill can authenticate to Huawei Cloud and may handle sensitive AK/SK credentials or tunnel tokens.

Mitigation: Prefer interactive login or temporary credentials, avoid printing credentials or tokens in logs or chat, and never store them in source-controlled files.

Risk: The skill can expose local services through remote tunnel URLs, including with anonymous access.

Mitigation: Review every exposed port and deny anonymous access unless the service is intentionally public.

Risk: The skill can start background host processes that continue exposing services.

Mitigation: Stop host/connect processes when finished and verify no unwanted DevBridge processes remain running.

Risk: The skill can delete tunnel resources, including delete-all operations.

Mitigation: Require manual confirmation before any delete or delete-all operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-devbridge-tunnel)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [CLI Command Reference](references/cli-command-reference.md)
- [REST API Reference](references/rest-api-reference.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Troubleshooting Guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, CLI examples, JSON snippets, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include long-running host/connect commands, authentication guidance, tunnel URLs, and cleanup instructions.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
