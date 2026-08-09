## Description:

BidHunter 标讯猎手 monitors Chinese public procurement and state-owned enterprise tender notices, compares them with configurable qualification rules, and generates bidability briefings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, bid agents, and suppliers use this skill to monitor supported Chinese tender platforms, classify notices as investable, not investable, or needing review against their own qualification rules, and prepare text or HTML briefings for decision review.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The pipeline contacts public procurement websites and stores fetched notices plus generated reports locally.

Mitigation: Run it only where network access and local storage are acceptable, and review generated cache and report files before sharing them.

Risk: Default qualification rules and placeholder entities may not match the user's real business scope or legal eligibility.

Mitigation: Customize qual_rules.json with current entities, capabilities, red alerts, and special rules before relying on bidability decisions.

Risk: Generated HTML reports can contain public notice data from external sources.

Mitigation: Sanitize or review generated HTML before opening, forwarding, or embedding it in other systems.

Risk: Scheduled runs or IM/email sharing can distribute duplicate or unreviewed briefings.

Mitigation: Confirm scheduled execution and sharing channels explicitly, and keep a human review step for generated briefings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/419597334-sudo/skills/bidhunter)
- [Supported platforms and configuration](references/platforms.md)
- [Qualification filter rules](references/filter_rules.md)
- [Tender field standard](references/field_standard.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and shell-command guidance with generated plain-text, HTML, JSONL, and CSV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local bid_cache, bid_reports, and optional bid_quotes outputs; users must customize qualification rules before relying on results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
