## Description:

Anrok (anrok.com). Use this skill for ANY Anrok request - searching and reading data. Whenever a task involves Anrok, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Anrok action schemas and run OOMOL-connected Anrok lookups for customers, products, filings, product mappings, tax categories, and transactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute changing network code.

Mitigation: Use official, versioned oo CLI installation instructions and prefer checksum or signature verification before running the installer.

Risk: The connector can read Anrok business and tax records from the connected account.

Mitigation: Connect only the Anrok account whose data the user intends the agent to read, and inspect the action schema before each connector run.

## Reference(s):

- [Anrok homepage](https://www.anrok.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-anrok)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Anrok connector schemas before constructing action payloads; connector responses are JSON when run with --json.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
