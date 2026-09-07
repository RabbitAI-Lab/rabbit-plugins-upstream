## Description:

Assesses a URL's Graceful Boundaries conformance level through direct HTTP inspection and provides a concrete implementation plan for reaching the next level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapsynapse](https://clawhub.ai/user/snapsynapse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API operators use this skill to evaluate how a public API or website communicates rate limits, refusal details, and recovery guidance. It produces an evidence-based assessment and practical steps for improving Graceful Boundaries conformance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct broad HTTP requests at user-provided URLs, which could unintentionally probe localhost, private networks, cloud metadata services, or authenticated systems.

Mitigation: Use it only for intentionally selected targets, preferably public HTTPS services, and avoid localhost, private network hosts, cloud metadata addresses, and authenticated services unless access is deliberate and contained.

Risk: HTTP inspection may expose ambient credentials if the execution environment automatically attaches cookies, authorization headers, proxy credentials, or client certificates.

Mitigation: Run audits from an isolated environment that does not attach credentials to outbound requests.

Risk: Trying to verify refusal behavior by forcing 429 responses could place unnecessary load on the target service.

Mitigation: Do not intentionally trigger rate limits; report Level 1 and Level 3 refusal behavior as unverifiable unless a natural refusal response is already available.

## Reference(s):

- [Graceful Boundaries Documentation](https://gracefulboundaries.dev)
- [ClawHub Skill Listing](https://clawhub.ai/snapsynapse/skills/graceful-boundaries)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown assessment with HTTP findings, gap analysis, implementation examples, and security notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON examples, HTTP header examples, and curl or equivalent shell commands.]

## Skill Version(s):

1.5.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
