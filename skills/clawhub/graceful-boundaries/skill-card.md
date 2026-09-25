## Description:

Assess APIs or websites for Graceful Boundaries conformance, rate-limit communication, structured refusals, and actionable steps to improve to the next conformance level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapsynapse](https://clawhub.ai/user/snapsynapse)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, API operators, and engineering teams use this skill to audit a URL's rate-limit communication and produce a prioritized Graceful Boundaries conformance assessment with implementation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to fetch discovery endpoints from user-provided services.

Mitigation: Use it only on URLs the user owns or has permission to audit, and keep requests lightweight.

Risk: Attempting to verify refusal behavior by forcing rate limits could create unwanted traffic or service disruption.

Mitigation: Do not deliberately trigger 429 responses; report refusal-format levels as unverifiable unless an actual refusal response is already available.

Risk: A service's self-declared conformance level may not match observable behavior.

Mitigation: Compare declared conformance with validated findings and clearly flag discrepancies.

## Reference(s):

- [Graceful Boundaries specification website](https://gracefulboundaries.dev)
- [ClawHub skill listing](https://clawhub.ai/snapsynapse/skills/graceful-boundaries)
- [Publisher profile](https://clawhub.ai/user/snapsynapse)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown assessment with HTTP findings, gap analysis, and implementation examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON examples, HTTP header examples, and optional shell command examples; does not install code or change the target service.]

## Skill Version(s):

1.5.6 (source: server release metadata and ClawHub manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
