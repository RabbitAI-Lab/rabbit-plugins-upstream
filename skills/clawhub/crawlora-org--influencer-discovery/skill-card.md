## Description:

Find and shortlist TikTok, Instagram, and YouTube creators for a campaign using Crawlora's creator datasets and live profile/content endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to source, refresh, compare, and rank public social media creators for campaign-fit decisions. It produces evidence-backed shortlists while marking unverified geography, audience, contact, and metric assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign search terms, creator identifiers, and the Crawlora API key are sent to Crawlora when the helper calls the API.

Mitigation: Use the skill only when that data sharing is acceptable, keep the API key in the environment, and do not paste secrets into prompts or outputs.

Risk: Creator contact or profile data could be over-collected or used without a legitimate outreach need.

Mitigation: Request email fields only when authorized, avoid guessing hidden contact information, and limit shortlist outputs to campaign-relevant data.

Risk: Dataset records and engagement metrics may be stale, incomplete, or platform-specific, which can make rankings misleading.

Mitigation: Refresh shortlisted profiles when currency matters, record sample sizes and dates, keep unavailable metrics unknown, and avoid comparing unlike engagement definitions across platforms.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/influencer-discovery)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables or CSV with optional shell command examples and evidence notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform handles, profile URLs, follower counts, refresh status, sampled content URLs, metric definitions, and fit rationale.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
