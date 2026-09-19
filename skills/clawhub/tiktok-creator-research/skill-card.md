## Description:

Vet public TikTok creators through live profile, post, video, comment, and user-search endpoints in Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to build current, evidence-backed TikTok creator shortlists from public profile, post, video, and comment data. It supports creator fit research while keeping public metrics, sampled content, and unknowns clearly separated from unsupported claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Crawlora API key is required to make live requests.

Mitigation: Keep the key in CRAWLORA_API_KEY, avoid placing it in prompts or command arguments, and rotate it if it may have been exposed.

Risk: TikTok search, profile, post, and comment parameters are sent to Crawlora.

Mitigation: Use the skill only for request parameters and public creator research data you are comfortable sending to Crawlora, and review Crawlora's terms and privacy practices first.

Risk: Search results and comment samples can be incomplete or stale.

Mitigation: Refresh candidate profiles before ranking, record refresh times and sample sizes, preserve unknowns, and avoid claims about demographics, authenticity, or conversion potential unless separately evidenced.

## Reference(s):

- [TikTok Creator Research Skill Page](https://clawhub.ai/crawlora-org/skills/tiktok-creator-research)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)
- [tiktok-creator-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, concise notes, and inline shell commands when API calls are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include refresh times, metric definitions, sample sizes, inclusion reasons, and unknowns.]

## Skill Version(s):

1.0.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
