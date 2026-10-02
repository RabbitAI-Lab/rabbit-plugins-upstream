## Description:

Generates LGD-III permission policies that classify agent tools as allowed, review-required, or denied and define four governance gates and execution budgets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (release listing); MIT (Python code); All rights reserved (documentation and theory)

## Use Case:

Developers and agent operators use this skill to generate and check tool-permission policies from agent capability lists or built-in presets before configuring an agent. Human reviewers must approve the resulting boundaries before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated permission boundaries may be unsuitable for a real agent.

Mitigation: Review and approve the generated policy before applying it; verify sensitive actions and tool classifications against the intended workflow.

Risk: Installation from an unintended source could introduce unreviewed content.

Mitigation: Install only from the intended release source.

Risk: Users may assume the code license also permits redistribution of the documentation and theory.

Mitigation: Check the separate all-rights-reserved notice for documentation and theory before reusing or redistributing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/gate-policy-generator)
- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Configuration, Guidance]

**Output Format:** [JSON permission policy or Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Policies list allowed, review-required, and denied tools, four gates, and loop/token budgets; checking reports missing gates or budgets.]

## Skill Version(s):

1.0.3 (source: ClawHub release; bundled frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
