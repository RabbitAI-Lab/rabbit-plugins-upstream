## Description:

IQ Core activates structured reasoning for complex problems through decomposition, multiple approaches, first-principles analysis, evidence ranking, contradiction checking, self-critique, and anti-hallucination guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent operators use this skill to apply structured reasoning before responding to complex, uncertain, or high-consequence tasks. It helps an agent decompose problems, compare solution paths, rank evidence, surface contradictions, and avoid presenting unsupported claims as facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional reasoning_log.py helper stores raw supplied text locally when used.

Mitigation: Use the helper only with non-sensitive content, or set a controlled IQ_CORE_LOG_PATH and redact secrets or personal data before logging.

Risk: Because the skill influences broad reasoning tasks, poor activation or unreviewed outputs could make incorrect guidance sound more authoritative.

Mitigation: Review outputs for evidence quality, unsupported claims, contradictions, and task-specific risk before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/iq-core)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown or plain text guidance, with optional code or shell command snippets when useful for the task.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an optional local reasoning_log.py helper that can write JSONL notes when explicitly used.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
