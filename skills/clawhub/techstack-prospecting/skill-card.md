## Description:

Find and qualify company websites by their detected technologies using Crawlora's tech-stack dataset and live website checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to find technology-matched websites and qualify existing domain lists for prospecting or integration targeting. They can compare stored detections with live checks and report evidence and uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queried domains, public URLs, and the Crawlora API key are sent to Crawlora.

Mitigation: Keep the key in the environment, use only documented endpoints, and review Crawlora's terms before large-scale checks.

Risk: Stored or homepage-only technology detections can be stale or incomplete, making prospect lists misleading.

Mitigation: Check shortlisted sites live, record observation dates and evidence, and preserve uncertainty when reporting results.

## Reference(s):

- [Tech-stack prospecting endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/techstack-prospecting)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Table or CSV with domain, matched technologies, detection evidence, freshness, fit rationale, and source URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves unknowns and distinguishes stored detections from live observations.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
