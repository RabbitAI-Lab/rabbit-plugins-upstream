## Description:

Operates Google Analytics through an OOMOL-connected account for reporting, metadata lookup, and managed property configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query GA4 accounts and properties, run standard and realtime reports, inspect metadata and quotas, and manage selected Google Analytics property settings through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses OOMOL as an intermediary for Google Analytics access.

Mitigation: Install and use it only when OOMOL-mediated access is acceptable for the analytics account and organization.

Risk: The first-time setup includes a CLI installer command.

Mitigation: Verify the oo CLI installer through OOMOL's official documentation before running it.

Risk: Write and destructive actions can change Google Analytics configuration.

Mitigation: Review exact payloads and require explicit user approval before write or destructive actions.

## Reference(s):

- [Google Analytics](https://analytics.google.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-google-analytics)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
