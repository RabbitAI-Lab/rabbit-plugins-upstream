## Description:

Generates LGD-III permission policies that classify agent tools as allowed, review-required, or denied and define four governance gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code); all rights reserved (documentation and theory)

## Use Case:

Developers and agent operators use this skill to generate JSON permission policies from tool manifests or presets and check that policies include the four gates and resource budgets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unclear deployment instructions could cause generated policies to be applied as live agent permissions without review.

Mitigation: Use the skill only to generate and inspect local policies; require explicit human approval before any runtime installation or enforcement.

Risk: Declared permissions and allowed tools overstate the local Python and file workflow.

Mitigation: Limit granted permissions and tools to those required for local generation and validation; confirm any broader access with the publisher.

## Reference(s):

- [Gate Policy Generator on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/gate-policy-generator)
- [Skill usage and policy format](artifact/README.md)

## Skill Output:

**Output Type(s):** [Configuration, Text]

**Output Format:** [JSON permission policy; text or JSON validation result; optional JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Policies include tool allow/review/deny lists, four gates, and loop and token budgets.]

## Skill Version(s):

1.0.4 (source: ClawHub release; bundled frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
