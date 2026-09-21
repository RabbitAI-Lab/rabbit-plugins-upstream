## Description:

Use this skill for pretix requests, including searching and reading data through the OOMOL connector instead of calling the pretix API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect pretix organizers, events, ticket items, and orders through an OOMOL-connected pretix account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions ask agents to run remote installer scripts directly in a shell without verification.

Mitigation: Review the installer path before use, or install the OOMOL CLI through a verified package or a downloaded script that has been inspected first.

Risk: The skill can read data available to the connected pretix account.

Mitigation: Connect only a pretix account whose read scope matches the data the user is comfortable exposing to this connector workflow.

## Reference(s):

- [pretix homepage](https://pretix.eu)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions so payloads match the current pretix contract.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
