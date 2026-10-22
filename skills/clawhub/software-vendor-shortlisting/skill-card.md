## Description:

Build a requirements-based software shortlist using Crawlora product discovery, public vendor pages, and review samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Software buyers and procurement teams use this skill to compare candidate vendors against their requirements, pricing assumptions, integrations, and review evidence before selecting demos or trials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, public page URLs, and the API key are sent to Crawlora; confidential requirements could be exposed if included in requests.

Mitigation: Use an approved Crawlora key and omit confidential internal requirements from requests unless that disclosure is authorized.

Risk: Sparse reviews, stale pricing, or unverified vendor claims can distort a purchasing shortlist.

Mitigation: Date and attribute claims, flag missing evidence and unknown costs, and confirm critical requirements in demos or trials.

## Reference(s):

- [Published skill on ClawHub](https://clawhub.ai/crawlora-org/skills/software-vendor-shortlisting)
- [Crawlora endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown shortlist with requirements matrix, pricing scenarios, sources, and demo questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes confirmed claims from unknowns and includes source dates.]

## Skill Version(s):

1.0.11 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
