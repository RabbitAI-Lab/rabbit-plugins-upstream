## Description:

Audits APIs and websites for Graceful Boundaries conformance, including structured refusals, 429 responses, limits discovery, and proactive rate-limit headers, then produces an evidence-based level assessment and improvement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapsynapse](https://clawhub.ai/user/snapsynapse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API operators use this skill to evaluate how a service communicates operational limits to agents and to get concrete steps for improving Graceful Boundaries conformance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes HTTP requests to user-provided URLs, which could inspect services the user is not authorized to assess.

Mitigation: Use it only on services the user is allowed to inspect, and avoid load testing or forcing rate-limit failures.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/snapsynapse/skills/graceful-boundaries)
- [Graceful Boundaries specification site](https://gracefulboundaries.dev)
- [Publisher profile](https://clawhub.ai/user/snapsynapse)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown assessment with HTTP findings, gap analysis, implementation examples, and security notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an evidence-based conformance level assessment without deliberately triggering rate limits.]

## Skill Version(s):

1.5.3 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
