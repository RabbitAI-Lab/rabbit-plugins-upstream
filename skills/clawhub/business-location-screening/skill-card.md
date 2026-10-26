## Description:

Compare user-supplied candidate locations for a local business using nearby competitors, public access signals, review samples, and available city-level context. Use for an early screen, not a lease or viability recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Small business owners and site selectors use this skill to compare a fixed set of candidate addresses or neighborhoods by nearby competitors, public access, review samples, and broad city-level context during early screening. Its findings help structure further due diligence before a lease decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Candidate locations and route anchors are shared with external mapping services.

Mitigation: Provide only locations and anchors that the user is comfortable sharing with Crawlora and the relevant mapping services.

Risk: API key exposure or unmonitored API credit usage.

Mitigation: Protect the API key and monitor credit usage.

Risk: Preliminary location signals could be mistaken for a lease or site-viability recommendation.

Mitigation: Treat results as preliminary research and check official, municipality-specific and property-level sources before making a lease decision.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/business-location-screening)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown evidence matrix with candidate comparisons, source notes, caveats, and follow-up data needs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps source coverage and retrieval times distinct; reports missing inputs and does not establish demand, revenue, zoning approval, commercial rent, or lease availability.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
