## Description:

输入关键词，用极目数据发现全部细分市场，按可配置标准评估进入价值，输出推荐清单（强烈推荐/推荐/谨慎考虑/不推荐）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, ecommerce operators, and market researchers use this skill to evaluate keyword-derived niche markets with Jiimore data. It helps compare demand, search volume, brand concentration, competition, growth, CPC, returns, and new-product success signals before prioritizing markets.

### Deployment Geography for Use:

Global; the documented Jiimore marketplace data coverage is US, JP, and DE.

## Known Risks and Mitigations:

Risk: Authenticated LinkFox requests can expose market-research keywords, API credentials, phone-based onboarding data, or billing actions to LinkFox services.

Mitigation: Install only when LinkFox is trusted for that data, keep endpoint environment variables unset or pointed to trusted official hosts, and require explicit confirmation before login, payment, or order commands.

Risk: Persistent local outputs can retain full Jiimore responses, LinkFox data, or QR files after the session.

Mitigation: Run the skill from an appropriate workspace and delete saved LinkFox data or QR files when they are no longer needed.

Risk: Automatic feedback reporting may include private research intent or result-quality details.

Mitigation: Avoid automatic feedback when conversations contain private market research or other confidential context.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-niche-market-recommendation)
- [LinkFox Publisher Profile](https://clawhub.ai/user/linkfox-ai)
- [Jiimore API Reference](skills/linkfox-jiimore-get-niche-info-by-keyword/references/api.md)
- [LinkFox Onboarding Guide](skills/linkfox-jiimore-get-niche-info-by-keyword/references/onboarding.md)
- [Niche Recommendation Method](skills/niche-recommendation-method/SKILL.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, saved JSON files, and concise follow-up guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long narrative reports and full LinkFox/Jiimore responses may be saved to local workspace files; missing source fields are labeled rather than fabricated.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
