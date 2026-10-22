## Description:

Find and shortlist TikTok, Instagram, YouTube, and Substack creators for a campaign using Crawlora's creator datasets and live profile and content endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and agents use this skill to discover creators and newsletter writers, compare campaign fit using public profile and content signals, and build evidence-backed shortlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign queries and creator lookup parameters are sent to Crawlora using an API key.

Mitigation: Use the skill only if that data transfer is acceptable; keep CRAWLORA_API_KEY secret.

Risk: Creator results can contain personal contact information.

Mitigation: Request contact emails only for legitimate outreach and restrict sharing of raw contact data.

Risk: Dataset records and incomplete platform metrics can misrepresent current creator fit.

Mitigation: Refresh promising profiles, date content samples, and label missing or unverified signals rather than treating them as zero or current.

## Reference(s):

- [ClawHub influencer-discovery release](https://clawhub.ai/crawlora-org/skills/influencer-discovery)
- [Crawlora](https://crawlora.net)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Creator shortlist, table, or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes profile links, dated content samples, audience signals, refresh status, and fit rationale; flags unknown or unverified signals.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
