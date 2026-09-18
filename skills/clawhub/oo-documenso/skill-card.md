## Description:

Documenso (documenso.com). Use this skill for ANY Documenso request — searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and search Documenso envelopes and templates through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to execute remote installer scripts.

Mitigation: Review setup instructions before installing, use a trusted and verifiable installation method, and do not let an agent run remote installer commands unattended.

Risk: Connector actions rely on the live schema and account connection state.

Mitigation: Inspect the action schema before preparing payloads and only use first-time setup steps after an authentication or connection failure.

## Reference(s):

- [ClawHub Documenso Skill](https://clawhub.ai/oomol/skills/oo-documenso)
- [Documenso Homepage](https://documenso.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for read-only Documenso connector actions and setup recovery steps.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
