## Description:

Clusters pasted log lines by template, counts frequencies, and highlights error signatures for incident triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use the skill to group pasted log lines, identify frequent and rare error patterns, and prioritize follow-up investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted logs may contain production secrets or credentials.

Mitigation: Avoid sharing secrets; redact any sensitive values before repeating log examples.

Risk: Heuristic normalization may merge distinct errors or misidentify a root cause.

Mitigation: Check representative lines and surrounding context before acting on a suggested cause.

## Reference(s):

- [Log Line Pattern Miner on ClawHub](https://clawhub.ai/hmahmadcs/skills/log-line-pattern-miner)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown summary and ranked pattern list, with optional regex or commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Counts, severity estimates, representative redacted examples, and follow-up questions]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
