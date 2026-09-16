## Description:

Sentry lets agents read Sentry data and update issue attributes through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Sentry organizations, projects, issues, events, releases, replays, alerts, integrations, and Sentry Apps, and to update issue attributes after confirming the requested change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute unverified code.

Mitigation: Use verified official oo CLI release instructions, prefer a pinned version or integrity check where available, and do not let an agent run remote installer scripts automatically.

Risk: The update_issue action can change Sentry issue status, assignment, or bookmarks.

Mitigation: Fetch the live action schema first and confirm the exact payload and expected effect with the user before running the write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sentry)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Sentry homepage](https://sentry.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions may be run directly; write actions require confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
