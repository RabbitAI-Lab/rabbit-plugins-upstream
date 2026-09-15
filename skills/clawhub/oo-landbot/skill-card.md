## Description:

Landbot (landbot.io). Use this skill for ANY Landbot request, including reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to work with Landbot through an OOMOL-connected account, including listing channels and customers, reading customer messages, sending text messages, and updating customer fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release uses an unsafe remote installer pattern for the oo CLI.

Mitigation: Install the CLI through a verifiable package or reviewed installer before running Landbot actions.

Risk: The skill grants broad local oo CLI authority for connected Landbot actions.

Mitigation: Review the requested action, inspect the live schema, and require explicit confirmation before any write action is run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-landbot)
- [Landbot Homepage](https://landbot.io)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
