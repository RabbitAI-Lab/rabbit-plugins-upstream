## Description:

Wachete helps agents operate Wachete monitors through an OOMOL-connected account, including monitor creation, retrieval, deletion, history access, folder listing, and notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Wachete website monitors through the OOMOL-connected oo CLI. It supports read workflows such as retrieving monitors, folder contents, notifications, and history, plus confirmed write workflows for creating, replacing, or deleting monitors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that may fetch unverified code.

Mitigation: Do not let an agent run installer commands automatically; use a verified package manager or review the installer with checksum or signature validation before execution.

Risk: Write actions can create or replace Wachete monitors.

Mitigation: Confirm the exact payload and expected effect with the user before running create_or_update_monitor.

Risk: Destructive actions can delete Wachete monitors.

Mitigation: Confirm the exact monitor ID and obtain explicit approval before running delete_monitor.

Risk: Connector permissions and account state determine what the agent can access or modify.

Mitigation: Install only when the publisher and Wachete connector permissions are trusted, and verify connection state before sensitive operations.

## Reference(s):

- [ClawHub Wachete Skill](https://clawhub.ai/oomol/skills/oo-wachete)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Wachete Homepage](https://www.wachete.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Wachete Icon](https://static.oomol.com/logo/third-party/wachete.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector calls that return JSON responses from Wachete.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
