## Description:

Provides Sentry access for reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Sentry alerts, issues, events, projects, releases, release health, replays, integrations, and Sentry Apps. They can update issue state after confirming the target and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote shell or PowerShell installer commands for the OOMOL CLI.

Mitigation: Review the installer or use an official safer installation method before running it.

Risk: The skill can update Sentry issue state through the update_issue action.

Mitigation: Confirm the exact issue target, live action schema, and payload before allowing the update.

Risk: The connected Sentry account may expose organization data or permit issue changes depending on granted scopes.

Mitigation: Connect Sentry with the minimum permissions needed for the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sentry)
- [Sentry homepage](https://sentry.io)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses include data and meta.executionId when commands are run.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
