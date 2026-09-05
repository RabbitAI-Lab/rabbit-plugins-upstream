## Description:

Assesses APIs and websites for Graceful Boundaries conformance and provides concrete guidance for improving rate-limit communication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapsynapse](https://clawhub.ai/user/snapsynapse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API operators use this skill to audit user-provided service URLs for Graceful Boundaries conformance and to get a prioritized implementation plan for improving rate-limit discovery, structured refusals, and proactive headers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes lightweight HTTP requests to URLs supplied for an audit.

Mitigation: Use it only on services where direct inspection is appropriate, and avoid URLs that should not receive automated requests.

Risk: Refusal behavior for 429 responses may be unverifiable without deliberately triggering a rate limit.

Mitigation: Report Level 1 and Level 3 refusal evidence as unverifiable unless a naturally occurring refusal response is available.

Risk: An audit result could produce incomplete or misleading implementation guidance if the inspected service exposes partial limit metadata.

Mitigation: Review the generated assessment before adopting changes, especially around published limits, same-origin guidance URLs, and Action Boundaries declarations.

## Reference(s):

- [Graceful Boundaries documentation](https://gracefulboundaries.dev)
- [ClawHub skill listing](https://clawhub.ai/snapsynapse/skills/graceful-boundaries)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Structured Markdown assessment with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes conformance level assessment, gap analysis, implementation examples, and security notes.]

## Skill Version(s):

1.5.4 (source: evidence.release.version; artifact skill metadata version 5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
