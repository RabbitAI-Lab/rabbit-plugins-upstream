## Description:

Search, inspect, and analyze prior OpenClaw sessions and transcript history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support operators, and OpenClaw users use this skill to locate prior sessions, inspect bounded transcript context, and support debugging of earlier model output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prior session transcripts may contain sensitive user or project information.

Mitigation: Use narrow searches and quote only the excerpts needed to answer the request.

Risk: Broad transcript review can expose more historical context than the task requires.

Mitigation: Start with bounded history reads and expand only when the result is insufficient.

Risk: Raw SQLite transcript inspection may bypass normal sanitized history views.

Mitigation: Reserve raw inspection for explicit debugging or forensic work with appropriate local access and read-only scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/session-logs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Concise Markdown answers with quoted excerpts and optional read-only diagnostic commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observed session, model, and timestamp details when lookup results support them.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
