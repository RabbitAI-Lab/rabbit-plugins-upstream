## Description:

A-share pre-market global risk signal radar that aggregates public market, geopolitics, calendar, China funding, domestic news, and macro data to produce directional scenarios, a 1-5 risk level, a shareable signal card, and optional Feishu delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill before the A-share market opens to fetch public global-market, macro, news, and funding signals, then generate a directional risk summary, risk level, shareable signal card, and optional Feishu push. Its financial analysis output is for reference and should not be treated as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial signals may be stale, incomplete, or misleading because they depend on public market and news data fetched at run time.

Mitigation: Treat reports as research context rather than investment advice, review source values before acting, and preserve the included disclaimer.

Risk: Optional Feishu delivery depends on webhook secrets and can publish generated analysis to a configured chat destination.

Mitigation: Use trusted Feishu webhook secrets, store them only in the intended secret manager or environment, and verify the destination before enabling pushes.

Risk: The local notify path can execute the file referenced by NOTIFY_HUB_SCRIPT when push_feishu.py is run with --send.

Mitigation: Leave NOTIFY_HUB_SCRIPT unset or point it only to a trusted notify-hub installation.

Risk: Some public data endpoints use HTTP or mixed endpoint schemes, which can reduce transport integrity if the skill is modified or run in an untrusted network.

Mitigation: Prefer HTTPS-only fetching where supported and run the skill from a trusted network environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xiyanjun/skills/hectorlee-global-risk-signal)
- [Server-resolved GitHub Source Repository](https://github.com/xiyanjun/hectorlee-global-risk-signal)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files]

**Output Format:** [Markdown-style agent guidance with bash commands; generated JSON reports, HTML signal cards, and Feishu card JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches public data sources at run time, writes date-stamped files under output/, and can optionally send a Feishu message when webhook or notify-hub configuration is supplied.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata; SKILL.md frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
