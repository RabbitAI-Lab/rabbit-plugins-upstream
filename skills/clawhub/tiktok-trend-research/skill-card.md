## Description:

Build evidence-backed TikTok trend briefs from current feeds, Creative Center rankings, hashtag data, and Explore categories through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, analysts, and developers use this skill to research TikTok trend signals for topics, hashtags, categories, countries, or periods and produce dated briefs with sample sizes, source IDs, filters, retrieval time, and caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok research inputs and a user-provided Crawlora API key to a third-party Crawlora API.

Mitigation: Confirm the data-sharing posture before use, keep the key in the environment, avoid sensitive search terms or request fields, and rotate the key if exposure is suspected.

Risk: TikTok trend surfaces are partial, time-sensitive, and can return limited or empty samples.

Mitigation: Report retrieval time, surface, filters, sample size, source IDs, and coverage caveats; label forecasts, content ideas, and causal claims as hypotheses.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/tiktok-trend-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief or table, optionally with shell command snippets and JSON observations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and live Crawlora/TikTok availability; outputs should include retrieval time, sample size, filters, source IDs, and coverage caveats.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
