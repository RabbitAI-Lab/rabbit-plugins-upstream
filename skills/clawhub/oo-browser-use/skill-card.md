## Description:

Browser Use helps an agent operate Browser Use Cloud through OOMOL's oo CLI to inspect action schemas, run browser-agent tasks, review sessions and messages, view billing information, and stop sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with a connected Browser Use account through OOMOL, including running browser automation tasks, checking Cloud sessions and messages, reviewing billing status, and stopping active sessions after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents pipe-to-shell installer commands for the oo CLI.

Mitigation: Install the CLI only after independently trusting and verifying the installer source, or use a reviewed installation path.

Risk: Browser-agent tasks can create Cloud sessions, perform website actions, or consume account credits.

Mitigation: Confirm the exact task, payload, expected effect, and spending impact before running task or session-changing actions.

Risk: Live action schemas can change over time.

Mitigation: Inspect the connector schema immediately before constructing each request payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-browser-use)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Browser Use Homepage](https://browser-use.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Browser Use Connection Setup](https://console.oomol.com/app-connections?provider=browser_use)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
