## Description:

Sentry (sentry.io). Use this skill for ANY Sentry request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering teams, and operations users use this skill to inspect Sentry organizations, projects, issues, events, releases, replays, alerts, integrations, and Sentry Apps, and to update issue attributes after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can affect the user's machine.

Mitigation: Review the installer path before use, prefer verified vendor instructions or a trusted package manager, and do not let an agent run curl|bash or irm|iex setup commands automatically.

Risk: The update_issue action can change Sentry issue attributes such as status, assignment, or bookmarks.

Mitigation: Confirm the exact write payload and expected effect with the user before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sentry)
- [Sentry homepage](https://sentry.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
