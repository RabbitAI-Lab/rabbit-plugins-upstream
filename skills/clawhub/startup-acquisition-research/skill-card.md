## Description:

Screens startups listed for sale using Crawlora's TrustMRR marketplace, stored company records, and daily metric history to support candidate shortlists and evidence-based diligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Acquisition researchers and prospective buyers use this skill to shortlist listed startups, compare asking prices and dated revenue history, and identify questions for further diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API queries send candidate-related research to Crawlora and require a Crawlora API key.

Mitigation: Keep the key in the environment and avoid including confidential buyer information or private records in queries.

Risk: Marketplace asking prices, revenue verification, and automated scores can be mistaken for audited financials or acquisition value.

Mitigation: Label evidence sources and dates, distinguish seller claims from verified metrics, and independently investigate costs, retention, and transferability.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/crawlora-org/skills/startup-acquisition-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [TrustMRR FAQ](https://trustmrr.com/faq)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown candidate table with source links and diligence questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dated metrics, defined calculations, evidence gaps, and discrepancies; does not place offers or contact sellers.]

## Skill Version(s):

1.0.11 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
