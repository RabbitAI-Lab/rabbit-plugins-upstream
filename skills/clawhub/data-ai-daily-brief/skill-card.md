## Description:

Turn any industry into a daily intelligence briefing by searching, filtering, writing, and delivering structured daily briefs through configured channels with formatting checks and a business review gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operations teams use this skill to generate recurring industry intelligence briefs from public sources, with a default Data+AI profile that can be adapted to other domains. The skill creates reviewed Markdown and HTML reports and can deliver channel-specific digests through configured adapters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Briefs may include sensitive internal content or be pushed to unintended delivery channels.

Mitigation: Review generated briefs before delivery and check config.json so only intended delivery channels are enabled.

Risk: Webhook, API, SMTP, or GitHub credentials may be exposed or over-privileged.

Mitigation: Store credentials in a secure secret store and grant only the least privilege needed for each channel.

Risk: Generated industry summaries can be incorrect, stale, duplicated, or insufficiently sourced.

Mitigation: Use the skill's recency, source-quality, deduplication, and business review gates before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/data-ai-daily-brief)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and HTML report files with channel-specific delivery payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes format pre-flight checks, source-link requirements, recency review, duplicate-push controls for supported channels, and configurable delivery adapters.]

## Skill Version(s):

5.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
