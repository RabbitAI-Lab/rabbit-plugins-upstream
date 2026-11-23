## Description:

Provides a read-only, evidence-driven assessment of a domain's DNS, TLS, HTTP headers, subdomains, exposed content, registration age, and compliance-publicity signals, with a deterministic I-Ching reading kept separate from conclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openmsg88](https://clawhub.ai/user/openmsg88)

### License/Terms of Use:

MIT

## Use Case:

Site owners, security reviewers, and developers use this skill to collect public evidence about a domain and produce a structured risk review. Compliance signals are informational hints rather than legal conclusions, and the hexagram is for entertainment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security scanners report requests to internal services, which could expose internal services.

Mitigation: Review the skill and its request targets before installing or running it, and restrict access to internal services as appropriate.

Risk: Security and compliance conclusions may be unreliable or unsupported, and the scanner's analysis is incomplete.

Mitigation: Verify report evidence independently, treat compliance results as hints rather than legal advice, and resolve the noted coverage gaps before relying on results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/openmsg88/skills/universal-domain-xuanping)
- [Risk Grading Criteria](references/RISK_GRADING.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Markdown risk report with structured JSON scan evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight risk dimensions; incomplete evidence is marked pending, and the hexagram is entertainment only.]

## Skill Version(s):

1.2.1 (source: frontmatter, CHANGELOG, released 2026-11-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
