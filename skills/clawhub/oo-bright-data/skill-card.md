## Description:

Enables an agent to inspect Bright Data connector schemas and run Bright Data read actions through OOMOL's oo CLI using a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Bright Data account status and marketplace dataset, snapshot, and view metadata through an OOMOL-connected Bright Data account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup tells users to run remote installer scripts directly in a shell.

Mitigation: Review the official OOMOL CLI installation documentation first, prefer a signed or package-manager install when available, and avoid running remote installer scripts from an elevated shell.

Risk: Connector actions depend on the connected account and live action schemas.

Mitigation: Inspect the authoritative action schema before building payloads, and require explicit user confirmation before running any action marked write or destructive.

## Reference(s):

- [ClawHub Bright Data skill](https://clawhub.ai/oomol/skills/oo-bright-data)
- [Bright Data homepage](https://brightdata.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Bright Data connection page](https://console.oomol.com/app-connections?provider=bright_data)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect live action schemas before running connector actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
