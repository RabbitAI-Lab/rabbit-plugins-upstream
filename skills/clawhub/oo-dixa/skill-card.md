## Description:

Dixa (dixa.com). Use this skill for ANY Dixa request: searching and reading data through the OOMOL-connected Dixa connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support, operations, and developer users can use this skill to inspect Dixa agents, admins, conversations, messages, end users, and presence statuses through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Inspect and validate installer scripts or use a verified installer before running them.

Risk: The connector can expose Dixa support data through the user's connected OOMOL account.

Mitigation: Limit requests to the Dixa records required for the task and avoid retrieving unnecessary support data.

## Reference(s):

- [ClawHub Dixa skill page](https://clawhub.ai/oomol/skills/oo-dixa)
- [Dixa homepage](https://www.dixa.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing Dixa connector requests.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
