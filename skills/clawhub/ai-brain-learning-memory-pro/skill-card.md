## Description:

Guides developers in designing three-tier agent memory, assessing a local memory setup, and planning safeguards against memory poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

AI developers and agent architects use this skill to plan tiered memory storage, integrate memory tools, configure review schedules, and assess memory quality and safety. It provides example code and a local evaluation script, not a deployed memory service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adopting the examples can leave persistent local memory files and assessment reports containing sensitive material.

Mitigation: Choose a non-sensitive memory directory and never store passwords, tokens, or private keys in memory files.

Risk: Stored memories may contain incorrect or untrusted instructions that influence later actions.

Mitigation: Review memory entries, verify their source, and require human confirmation before consequential actions.

## Reference(s):

- [Research sources and engineering implications](references/调研出处与证据.md)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-brain-learning-memory-pro)
- [LGD theory (referenced by skill)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Python examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The optional local evaluation script writes a six-dimension JSON assessment when run.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
