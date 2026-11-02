## Description:

当用户需要做小红书竞品研究、小红书竞品分析、同赛道观察、内容角度对比、内容策略对比或品牌内容调研时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External brand teams, MCNs, content operators, and creators use this skill to research Xiaohongshu competitors, monitor a content niche, compare content angles and strategies, and study brand content using a keyword or topic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX.

Mitigation: Avoid including confidential plans or other sensitive information in search terms.

Risk: The skill requires a SocialDataX API key at runtime.

Mitigation: Keep SOCIALDATAX_API_KEY protected in the runtime environment and out of prompts and shared output.

Risk: Collecting more pages can increase usage costs.

Mitigation: Set page limits or an item cap, such as --pages or --max-items, to control collection size.

Risk: The documented read-only behavior is not enforced by the skill Markdown when using the external package.

Mitigation: Use a reviewed, fixed CLI package version and confirm its behavior before running it.

## Reference(s):

- [SocialDataX skill and API key access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-competitor-research-v2)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Shell commands]

**Output Format:** [Markdown research summary with sample titles, authors or accounts, links or IDs, and content angles; Bash CLI examples when relevant.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search coverage is limited by the requested page count or item cap; present results as samples rather than complete platform coverage.]

## Skill Version(s):

0.1.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
