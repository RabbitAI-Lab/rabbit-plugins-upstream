## Description:

Ops Maintenance helps agents run local, remote, and cluster operations checks including health, logs, performance, password expiry, alerts, Docker, SSL, security audit, and network diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fish1981bimmer](https://clawhub.ai/user/fish1981bimmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect local or SSH-accessible servers, generate operations reports, audit configuration and security posture, and manage monitoring alerts. It should be used with controlled infrastructure access because it can run commands locally and remotely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad local and remote command authority can affect real infrastructure if the skill is given unrestricted shell or SSH access.

Mitigation: Install and run it only in a controlled environment with least-privilege SSH accounts and scoped server configuration.

Risk: Generic execution paths and network diagnostic inputs may be unsafe when driven by untrusted or loosely validated input.

Mitigation: Avoid generic exec and diagnostic flows unless inputs are fixed to argument arrays and strict validation.

Risk: SSH, SMTP, webhook, or notification secrets may be exposed if stored in plain configuration files or available through default local keys.

Mitigation: Keep secrets out of plain config files, avoid production-wide default credentials, and verify host-key checking plus key-file permissions before connecting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fish1981bimmer/skills/ops-maintenance)
- [Architecture documentation](artifact/doc/ARCHITECTURE.md)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with command output blocks, tables, recommendations, and optional JSON output for supported commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read server configuration and use SSH or local shell access according to the invoked maintenance task.]

## Skill Version(s):

3.3.10 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
