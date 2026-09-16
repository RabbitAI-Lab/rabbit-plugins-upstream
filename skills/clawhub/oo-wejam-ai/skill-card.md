## Description:

Jam lets an agent inspect Jam connector schemas and export one page of Jam training data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Jam through the oo CLI, inspect the live connector action schema, and export Jam training data for reporting or BI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer pipelines that can execute code on the user's machine.

Mitigation: Prefer an official, versioned oo CLI installation method with signature or checksum verification before using the skill.

Risk: The skill operates against whichever Jam account is connected through OOMOL.

Mitigation: Connect only the Jam account intended for the task and review the live action schema before running connector actions.

## Reference(s):

- [Jam homepage](https://wejam.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wejam-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing Jam requests.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
