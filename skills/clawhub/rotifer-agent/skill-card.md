## Description:

Build AI Agents from Genes by decomposing intent into capability units, selecting Genes from Arena rankings, composing a Rotifer Genome with Seq/Par/Cond/Try/TryPool strategies, and validating the pipeline end to end.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design Rotifer-specific agents from Genes, choose composition strategies, create the agent with the Rotifer CLI, and validate the result. It is intended for Rotifer Genome workflows, not for general agent frameworks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an assistant to install or run the Rotifer CLI, including npm-based commands.

Mitigation: Review proposed install and execution commands before approving them.

Risk: Rotifer commands can create or modify project-local Gene files and agent definitions.

Mitigation: Inspect planned file changes before approving create, overwrite, or publish actions.

Risk: Registry and Arena queries may contact the public Rotifer API.

Mitigation: Confirm that outbound registry lookups are acceptable for the workspace before running them.

## Reference(s):

- [Rotifer skill page](https://clawhub.ai/xiaoba-dev/skills/rotifer-agent)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Playground repository](https://github.com/rotifer-protocol/rotifer-playground)
- [rotifer-guide](https://clawhub.ai/skills/rotifer-guide)
- [rotifer-arena](https://clawhub.ai/skills/rotifer-arena)
- [rotifer-self-evolving-agent](https://clawhub.ai/skills/rotifer-self-evolving-agent)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with tables, inline shell commands, and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Rotifer CLI commands that read and write project-local Gene and Agent files.]

## Skill Version(s):

1.2.1 (source: server release metadata and clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
