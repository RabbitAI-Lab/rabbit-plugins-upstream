## Description:

Find and shortlist TikTok, Instagram, and YouTube creators for a campaign using Crawlora's creator datasets and live profile/content endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, creator partnerships, and campaign teams use this skill to source, refresh, compare, and document public creator candidates across TikTok, Instagram, and YouTube. It helps produce evidence-backed shortlists while marking dataset-only, unavailable, or unverified assumptions clearly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign search terms, creator identifiers, and the Crawlora API key are sent to Crawlora when using the helper.

Mitigation: Install and run the skill only when that data sharing is acceptable, and keep the API key in the environment rather than embedding it in prompts or files.

Risk: Optional contact-email access can expose personal contact data for creators.

Mitigation: Request contact emails only with a legitimate outreach basis and handle them under applicable privacy and anti-spam rules.

Risk: Dataset records and engagement metrics can be incomplete, stale, or populated for only a subset of creators.

Mitigation: Refresh shortlisted profiles, preserve dataset timestamps, label dataset-only candidates, and keep absent metrics unknown rather than treating them as zero.

## Reference(s):

- [Influencer Discovery Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/influencer-discovery)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown tables, concise prose, CSV when requested, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shortlists include platform, handle or channel ID, profile URL, topic-fit evidence, follower counts, refresh status, sampled content URLs, metric definitions, and fit rationale.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
