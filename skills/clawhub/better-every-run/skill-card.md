## Description:

Better Every Run: capture explicit /ber corrections, review them, and promote only the lessons that deserve durable memory, skill rules, or evals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leostehlik](https://clawhub.ai/user/leostehlik)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to capture explicit correction lessons, review whether they should become durable memory, skill behavior, or eval coverage, and report what changed without silently turning ordinary chat into permanent memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Correction lessons can contain secrets, sensitive personal data, or private workspace details if users choose to record them.

Mitigation: Avoid putting secrets or sensitive personal data in /ber lessons, review lesson cards before promotion, and keep .better-every-run/ private and out of published packages.

Risk: Unreviewed lessons could incorrectly influence durable memory, skill behavior, or eval coverage.

Mitigation: Use the disclosed review flow before durable promotion, and rely on scanner verdicts to block promotion when findings or warnings are present.

## Reference(s):

- [Better Every Run workflow](references/workflow.md)
- [Better Every Run report template](references/report-template.md)
- [Before/after correction artifact](examples/before-after-correction.md)
- [ClawHub skill page](https://clawhub.ai/leostehlik/skills/better-every-run)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise chat reports and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports local lesson status and reviewed durable-promotion outcomes.]

## Skill Version(s):

0.6.0 (source: SKILL.md metadata, CHANGELOG, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
