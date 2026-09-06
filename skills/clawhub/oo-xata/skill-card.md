## Description:

Provides guidance and oo CLI commands for reading Xata organizations, projects, branches, and regions through an OOMOL-connected Xata account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Xata account resources through an OOMOL-connected account, including organizations, projects, branches, and available regions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent access to Xata account data through the oo CLI when the user has connected Xata.

Mitigation: Install only when the user trusts OOMOL and wants agent-mediated access to their Xata account.

Risk: Connector actions or future schema changes could involve creating, updating, deleting, or overwriting Xata data.

Mitigation: Review the live connector schema and exact payload, and require explicit user confirmation before any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-xata)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Xata Homepage](https://xata.io/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.1 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
