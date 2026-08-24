## Description:

Use when activating the adaptive agent OS: open-minded skill use, data-first behavior, stepwise reasoning, self-correction, anti-repetition, and agentic task execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Agents and agent builders use Aurum Brain as a broad behavior overlay for data-first reasoning, stepwise execution, self-correction, and concise responses across general tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is a broad behavior overlay that may influence many agent responses.

Mitigation: Install it only when broad reasoning and response-quality guidance is desired, and narrow activation criteria before publication when a smaller scope is required.

Risk: The included logger can persist raw task text in local JSONL records.

Mitigation: Avoid using the logger with secrets or private customer data, redact sensitive inputs before logging, and configure explicit file-write permissions or a controlled log path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/aurum-brain)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with optional shell commands and JSONL log entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an optional local reasoning/self-check logger that writes JSONL records.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
