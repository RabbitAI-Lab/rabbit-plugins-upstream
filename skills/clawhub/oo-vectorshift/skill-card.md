## Description:

VectorShift lets an agent list, inspect, and run VectorShift pipelines through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage VectorShift pipelines from an agent workflow: list or fetch pipelines, run a single pipeline, or bulk-run pipeline executions after checking the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remotely downloaded installer directly in a shell.

Mitigation: Review the installer source or install the oo CLI through a trusted package manager or official manual process before using the skill.

Risk: State-changing VectorShift actions can run pipeline executions.

Mitigation: Fetch the live connector schema first and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [VectorShift homepage](https://vectorshift.ai)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action results are JSON responses with data and meta.executionId when commands run.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
