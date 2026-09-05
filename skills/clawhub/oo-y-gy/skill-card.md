## Description:

Y.GY enables agents to read, create, update, and delete Y.GY short links through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Y.GY short links from an agent session, including create, list, read, update, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update Y.GY short links through the connected OOMOL account.

Mitigation: Review the exact payload and expected effect with the user before running any write action.

Risk: Destructive actions can delete Y.GY short links.

Mitigation: Confirm the target identifier and obtain explicit approval before running delete actions.

## Reference(s):

- [Y.GY homepage](https://app.y.gy)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
