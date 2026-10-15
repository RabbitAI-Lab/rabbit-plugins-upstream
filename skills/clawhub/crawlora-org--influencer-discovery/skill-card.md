## Description:

Find and shortlist TikTok, Instagram, YouTube, and Substack creators for a campaign using Crawlora's creator datasets and live profile/content endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and campaign teams use this skill to discover creators and newsletter writers, compare public campaign-fit signals, and prepare evidence-backed shortlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, creator identifiers, and the API key are sent to Crawlora.

Mitigation: Use the skill only when that disclosure is acceptable; keep the key in an environment variable and out of shared logs and shell history.

Risk: Public creator metrics and geography may be incomplete, dated, or mistaken for audience demographics.

Mitigation: Review shortlists against source profiles, label dataset-only results and retrieval times, and do not infer audience demographics from creator location.

## Reference(s):

- [Influencer Discovery on ClawHub](https://clawhub.ai/crawlora-org/skills/influencer-discovery)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, Guidance]

**Output Format:** [Shortlist as a Markdown table or CSV, with supporting rationale]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes profile links, public audience signals, content samples, and freshness labels; does not establish audience demographics.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
