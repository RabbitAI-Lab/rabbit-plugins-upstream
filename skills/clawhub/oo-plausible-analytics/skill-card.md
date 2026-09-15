## Description:

Plausible Analytics skill for querying historical, real-time, breakdown, and timeseries analytics and recording Plausible events through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analytics operators use this skill to inspect Plausible Analytics schemas, query site analytics, generate breakdown or timeseries reports, and record pageviews or custom events through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents mainly as read-oriented while record_event can write analytics events.

Mitigation: Treat record_event as a write operation and confirm the site, event name, URL, properties, and intended analytics effect before running it.

Risk: Installer examples include pipe-to-shell commands for installing the oo CLI.

Mitigation: Avoid pipe-to-shell installation unless the installer source and contents have been independently verified.

Risk: The skill relies on OOMOL and the oo CLI using a Plausible-connected account.

Mitigation: Install only after confirming trust in OOMOL and the oo CLI with the connected Plausible account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-plausible-analytics)
- [Plausible Analytics homepage](https://plausible.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, connector action payloads, schema-inspection guidance, analytics summaries, and user-confirmation prompts for write operations.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
