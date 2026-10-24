## Description:

Randomly generate a structured, configurable study-practice plan (学习实践表) as a Markdown table, plain text, or JSON, with a seed option for reproducible results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Learners and developers can use the skill to create configurable study schedules with a topic, practice task, and session duration for each time slot. A seed can be supplied to reproduce a plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writing to an output path may replace an existing file.

Mitigation: Choose and check the output path before running the generator.

## Reference(s):

- [Usage guide](references/usage-guide.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Verification method](references/verification-method.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [ClawHub release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-study-plan-generate)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown table, plain text, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured day-and-time-slot plan with a topic, practice item, and session duration per slot; optional seed enables reproducibility.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
