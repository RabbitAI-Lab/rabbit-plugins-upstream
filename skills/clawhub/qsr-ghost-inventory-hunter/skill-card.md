## Description:

Identifies unaccounted inventory loss in restaurant operations by cross-referencing sales volume against theoretical recipe yields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mcphersonai](https://clawhub.ai/user/mcphersonai)

### License/Terms of Use:

CC BY-NC 4.0

## Use Case:

Restaurant and franchise operators use this skill to investigate unexplained inventory variance for one high-cost item at a time. It compares sales, recipe yields, delivery receipts, inventory counts, and waste tracking to identify likely causes such as over-portioning, unrecorded waste, prep errors, receiving discrepancies, or theft.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may process or retain restaurant sales, inventory, waste, and cost figures while helping track variance.

Mitigation: Invoke the skill intentionally and avoid sharing sensitive business data that should not be retained in agent memory.

Risk: Inventory variance findings may point toward theft or operational misconduct.

Mitigation: Use the skill's output as an investigation aid, review the underlying records, and avoid treating the result as an accusation without independent confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mcphersonai/skills/qsr-ghost-inventory-hunter)
- [McPherson AI](https://mcphersonai.com)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational guidance and structured Markdown investigation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include calculated inventory variance, estimated dollar loss, probable cause, recommended action, and follow-up date.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
