## Description:

Skillify helps agents turn qualified, repeatable workflows into portable Agent Skill packages with concise instructions, trigger-focused metadata, gotchas, and evals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent maintainers use this skill after real execution evidence exists to package a proven repeatable workflow into a durable portable Agent Skill. It guides them to extract the invariant procedure, remove incidental project context, add realistic evals, and state graduation status truthfully.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skills can preserve incorrect or misleading procedures as durable agent instructions.

Mitigation: Review the generated skill package and scan it before deployment.

Risk: A one-off successful procedure could be mislabeled as proven or installed before it has reuse evidence.

Mitigation: Require the evidence gate, realistic evals, and a separate graduation decision before calling the skill proven or deploying it.

## Reference(s):

- [Overpowered suite](https://github.com/raguets/overpowered)
- [ClawHub skill page](https://clawhub.ai/raguets/skills/skillify)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown skill instructions plus JSON evaluation specifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a proposed skill package for review; deployment remains a separate graduation decision.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
