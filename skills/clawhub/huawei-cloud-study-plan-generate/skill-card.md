## Description:

Generates configurable study-practice schedules with varied topics, concrete exercises, non-overlapping time slots, and Markdown, plain-text, or JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and learners use the skill to create structured study schedules and practice plans from a built-in or custom topic pool. They can provide a seed to reproduce a plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Choosing an existing output path can replace its contents.

Mitigation: Check the target path before using --output; choose a new filename or back up any file that should be preserved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-study-plan-generate)
- [Usage Guide](artifact/references/usage-guide.md)
- [Verification Method](artifact/references/verification-method.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Data Flow](artifact/references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown table, plain text, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Configurable by days, slots per day, topics, session length, start date, seed, format, and optional output file; a fixed seed makes the plan reproducible.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
