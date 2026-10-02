## Description:

Find and shortlist TikTok, Instagram, YouTube, and Substack creators for campaigns using Crawlora's creator datasets and live profile and content endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creator-sourcing agents use this skill to discover, compare, and shortlist creators and newsletter writers for campaigns, with dated public evidence for each candidate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign search terms and the API key are sent to Crawlora.

Mitigation: Use this skill only if that disclosure is acceptable; keep the key in the environment and avoid including sensitive campaign details in queries.

Risk: Optional contact-email retrieval can expose personal contact information.

Mitigation: Retrieve email addresses only for legitimate outreach and follow applicable privacy and anti-spam rules.

Risk: Dataset records and some audience metrics may be stale, missing, or incomplete.

Mitigation: Refresh shortlisted profiles, record retrieval times and sample sizes, and label missing or unverified signals rather than treating them as zero or current.

## Reference(s):

- [Influencer Discovery on ClawHub](https://clawhub.ai/crawlora-org/skills/influencer-discovery)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Crawlora](https://crawlora.net)
- [Supported endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Shortlist, table, or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes profile links, public audience signals, sampled content, retrieval dates, metric definitions, and fit rationale; marks unknown or unverified signals.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
