## Description:

Use this skill to search and read Airmeet data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Airmeet event data through an OOMOL-connected account. It supports listing Airmeet events, booths, registration fields, sessions, and tracks after checking the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Before installation, prefer an official signed package or download-and-verify flow, and run remote installer commands only after independently trusting OOMOL's installer path.

Risk: The skill depends on an OOMOL-connected Airmeet account and live connector schemas, so authentication or connection state can block use.

Mitigation: Run setup or reconnect Airmeet only after a command fails with a matching authentication, scope, credential, app, or billing error.

## Reference(s):

- [ClawHub Airmeet skill page](https://clawhub.ai/oomol/skills/oo-airmeet)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Airmeet homepage](https://www.airmeet.com/)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Airmeet connection page](https://console.oomol.com/app-connections?provider=airmeet)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
