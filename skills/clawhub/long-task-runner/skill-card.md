## Description:

Run slow local commands and queues with bounded logs, safe recovery, and artifact checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dhzyw](https://clawhub.ai/user/dhzyw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding-agent users use this skill to run long local commands and queues with bounded logs, explicit recovery rules, and artifact checks while preserving model attention for planning, exceptions, and final review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run local commands, and child processes inherit the current account environment and access.

Mitigation: Install from a pinned, verified source where possible; review each job spec before starting it; and use only commands the user would be comfortable running directly.

Risk: Untrusted validators or job specs could execute unwanted local behavior.

Mitigation: Inspect validators and command arguments before use, keep work in a constrained project directory, and avoid passing secrets unless the task explicitly requires them.

Risk: Remote watching may be mistaken for remote cancellation, submission, or billing control.

Mitigation: Treat remote watching as status polling only; do not assume local cancellation cancels remote work or costs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dhzyw/skills/long-task-runner)
- [Skill instructions](SKILL.md)
- [README](README.md)
- [Job configuration](references/job-spec.md)
- [Scenario guidance](references/scenarios.md)
- [Host waiting boundaries](references/host-waiting.md)
- [Task handoff guidance](references/task-handoff.md)
- [Optional compression layer](references/optional-compression.md)
- [Task handoff template](assets/task-handoff-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, JSON job specifications, and bounded status summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce job state files, rotating logs, validation reports, and compact handoff templates when the user opts into handoff workflows.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
