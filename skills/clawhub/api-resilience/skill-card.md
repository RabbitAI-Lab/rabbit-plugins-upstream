## Description:

Guides agents and developers in handling unstable external APIs with backoff and jitter, rate limiting, circuit breaking, and fallback patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (.py code only); documentation and theory: All rights reserved

## Use Case:

Developers and agent builders use this skill to plan safer retries, rate limits, circuit breakers, and fallbacks when third-party services time out, throttle requests, or become unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Poorly tuned retries, fallbacks, or circuit breakers could worsen production outages or hide failures.

Mitigation: Review the guidance and validate retry limits, backoff, and fallback behavior against the target service before production changes.

Risk: Installing a different copy or overlooking bilingual instructions could lead to unintended behavior.

Mitigation: Confirm the publisher and intended release source, and review the Chinese and bilingual documentation before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/api-resilience)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Text or Markdown guidance and example Python commands; optional JSON lines from the local demo]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled demo simulates failures and recovery rather than integrating with a live API.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
