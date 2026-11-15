## Description:

Build a Rotifer Agent from Genes — decompose intent into capability units, pick Genes by Arena F(g), compose a Rotifer Genome, create the Agent and test it. Use when the user is working with Rotifer specifically: "Rotifer Agent", "compose Genes", "Rotifer Genome", "Gene composition", "rotifer agent create". Do NOT use for general agent frameworks, or when the words Seq / Par / Cond / Try appear as ordinary programming terms — in Rotifer those name Genome composition strategies, and this Skill applies only when the user is composing Rotifer Genes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when they want to design a Rotifer Agent for a specific task. It helps decompose the task into Genes, select and compose them, then create and validate the Agent through Rotifer workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security guidance notes that CLI bootstrap may write to the npm cache and related metadata or logs outside the project.

Mitigation: Review those npm cache and metadata writes before bootstrapping; configure a cache location that fits the user's workspace expectations if needed.

Risk: The security analysis is partial because three local path-like references did not match bundled artifacts.

Mitigation: Review the unmatched references and relevant release files before relying on the scan coverage.

## Reference(s):

- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Playground repository](https://github.com/rotifer-protocol/rotifer-playground)
- [Rotifer Protocol specification](https://github.com/rotifer-protocol/rotifer-spec)
- [ClawHub release page](https://clawhub.ai/xiaoba-dev/skills/rotifer-agent)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown with inline tables, shell commands, and Rotifer composition examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for composing an Agent from 2–6 Genes; Agent configuration is created through the Rotifer CLI.]

## Skill Version(s):

1.2.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
