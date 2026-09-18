## Description:

Algolia (algolia.com). Use this skill for ANY Algolia request: reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Algolia connector schemas, search or browse indices, retrieve records, and perform confirmed record, rule, or synonym changes through an OOMOL-connected Algolia account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may direct users to execute remote installer scripts directly.

Mitigation: Review installer guidance before installation and prefer a trusted, verifiable installation method for the oo CLI.

Risk: Write and destructive Algolia actions can change or remove indexed data.

Mitigation: Confirm the exact Algolia payload, target index, and expected effect with the user before running write or delete actions.

## Reference(s):

- [Algolia homepage](https://www.algolia.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-algolia)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing Algolia action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
