## Description:

BrowserStack (browserstack.com). Use this skill for BrowserStack requests that read, create, or update BrowserStack data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and release teams use this skill to inspect BrowserStack action schemas, retrieve Automate session and build information, and update session pass/fail status through an OOMOL-connected BrowserStack account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Review the installer source and prefer a pinned, verifiable installation path before running setup commands.

Risk: The update_session_status action can change BrowserStack session state.

Mitigation: Confirm the exact BrowserStack write-action payload and intended effect with the user before allowing the status update.

## Reference(s):

- [ClawHub BrowserStack Skill](https://clawhub.ai/oomol/skills/oo-browserstack)
- [BrowserStack Homepage](https://www.browserstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [BrowserStack Connection Setup](https://console.oomol.com/app-connections?provider=browserstack)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include BrowserStack action schemas, connector responses, session details, build listings, status-update payloads, and setup or billing guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
