## Description:

Turn any industry into a daily intelligence briefing: an AI agent searches, filters, writes, and delivers structured daily briefs to configured channels with machine-checked formatting and a business review gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to produce recurring industry intelligence briefs from public sources, with a Data+AI profile included as the default configuration. It supports brief generation, format checks, review before publishing, and delivery to configured channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated briefs may be delivered to third-party chat, email, or publishing services using configured credentials.

Mitigation: Review config.json destinations and enable only intended channels before running delivery.

Risk: Industry summaries can include incorrect, stale, or weakly sourced information if review is skipped.

Mitigation: Use the built-in business review gate, recency checks, and source-quality checks before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/data-ai-daily-brief)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown brief, optional HTML page, channel payloads, and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated briefs include source links, sectioned summaries, format checks, and channel-specific delivery payloads when configured.]

## Skill Version(s):

5.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
