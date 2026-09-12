## Description:

Dependency checkup for owner-operators that identifies who can unilaterally change rules, pricing, access, supply, payment, or delivery conditions, and requires switching cost and switching time for every high-risk dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External owner-operators and small-business leaders use this skill to map production-side dependencies across channels, premises and licences, key people, suppliers, and payment rails. It helps them classify dependency severity and choose practical next actions such as preparing a Plan B, recording expiry dates, or quantifying unresolved switching costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may retain commercially sensitive details about a user's business dependencies in persistent memory.

Mitigation: Install only where memory use is approved and inspectable, and delete saved records when they are no longer needed.

Risk: The skill may read shared memory outside its own directory.

Mitigation: Use it in environments where agent memory is isolated or where access to shared memory can be reviewed before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-dependency)
- [理论底座](references/理论底座.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown dependency assessment report with tables, severity labels, action items, and numbered next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses concise Chinese business-facing prose and may ask one multiple-choice clarification question when required information is missing.]

## Skill Version(s):

0.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
