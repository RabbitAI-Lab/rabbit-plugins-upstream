## Description:

Ops Maintenance helps agents run local and remote operations checks for health, security, logs, configuration changes, alerts, scheduled patrols, Docker container health, SSL certificates, networking, services, and file transfer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fish1981bimmer](https://clawhub.ai/user/fish1981bimmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect server health, diagnose logs and network issues, review configuration drift, generate operations reports, and manage alerts across local or SSH-accessible systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access remote servers, run command-based diagnostics, transfer files, store credentials, and send notifications.

Mitigation: Use only in controlled operations environments with explicit least-privilege SSH keys, trusted inputs, and reviewed target scopes.

Risk: Broad cluster targets and command-based workflows can affect many systems or expose sensitive operational data.

Mitigation: Require human review for cluster-wide actions, upload/download paths, configuration snapshots, and diagnostics before execution.

Risk: Webhook and SMTP notification settings may contain sensitive secrets.

Mitigation: Avoid storing sensitive notification credentials until persistence and secret-handling controls are confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fish1981bimmer/skills/ops-maintenance)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON reports with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational findings, alert summaries, audit entries, and generated configuration or command guidance.]

## Skill Version(s):

3.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
