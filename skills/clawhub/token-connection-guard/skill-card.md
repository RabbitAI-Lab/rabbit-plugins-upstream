## Description:

Helps OpenClaw agents conserve tokens, context, requests, and time by using batching, context compression, retry backoff, circuit breakers, cache reuse, provider failover, and graceful degradation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to guide OpenClaw resource management, request retry behavior, provider failover, and context compression during normal agent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Caching or failure logging in an agent environment could retain secrets or stale real-time data.

Mitigation: Configure agent caching and logs to avoid storing secrets, redact sensitive values, and refresh or bypass cached data when freshness matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/token-connection-guard)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown guidance and operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavioral guidance only; no executable code is included in the artifact.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
