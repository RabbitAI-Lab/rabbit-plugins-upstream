## Description:

Find and shortlist TikTok, Instagram, and YouTube creators for a campaign using Crawlora's creator datasets and live profile/content endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, campaign operators, and agents use this skill to translate a campaign brief into a bounded, evidence-backed shortlist of TikTok, Instagram, and YouTube creators. It supports creator sourcing, profile refreshes, content sampling, metric qualification, and shortlist/table/CSV reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to an unvalidated destination if CRAWLORA_API_BASE is set.

Mitigation: Keep CRAWLORA_API_BASE unset unless the destination is fully trusted, and use a narrowly scoped Crawlora key.

Risk: Returned contact emails may be personal data.

Mitigation: Access contact emails only when lawful and necessary for the campaign, and avoid guessing hidden contact information.

Risk: Dataset results and engagement metrics may be stale, incomplete, or platform-specific.

Mitigation: Refresh shortlisted creators where possible, preserve timestamps, label dataset-only candidates, and avoid comparing unlike engagement definitions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown, tables, CSV, shell commands, and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shortlists should include platform, handle or channel ID, profile URL, topic-fit evidence, follower count, refresh status, sampled content URLs, metric definitions, and fit rationale.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
