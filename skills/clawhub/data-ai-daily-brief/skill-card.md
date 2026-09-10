## Description:

Turn any industry into a daily intelligence briefing: an AI agent searches, filters, writes, and delivers structured daily briefs to configured channels with formatting checks and a business review gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operations teams use this skill to produce recurring industry intelligence briefs from public sources. It is suited for daily newsletters or internal briefings that need source tracing, recency checks, structured sections, Markdown and HTML outputs, and optional delivery to configured channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create daily briefing files and send content through configured delivery channels.

Mitigation: Review config.json, enabled adapters, and local scripts before allowing delivery; keep the business review gate enabled.

Risk: Delivery adapters may use sensitive tokens or webhooks for GitHub, SMTP, Telegram, or chat services.

Mitigation: Provide only the credentials needed for intended channels and verify channel configuration before execution.

Risk: Daily briefs can become misleading if stale or weakly sourced items pass through.

Mitigation: Apply the skill's recency window, source tracing, deduplication, and pre-flight checks before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/data-ai-daily-brief)
- [Publisher Profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown brief, optional HTML page, channel payloads, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The brief uses fixed sections, source links, WeChat summary lines, item counts, and a mandatory pre-flight format check before delivery.]

## Skill Version(s):

5.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
