## Description:

当用户需要做抖音趋势洞察、抖音趋势分析、热点观察、内容方向判断、趋势线索归纳或营销灵感整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand researchers, creators, and marketing teams use this skill to inspect Douyin hot-search and keyword-search signals, then summarize trends, content angles, representative samples, and follow-up questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill executes npm/npx code and sends Douyin search parameters to SocialDataX.

Mitigation: Install and run it only after confirming trust in SocialDataX and in the configured SOCIALDATAX_API_KEY billing or authentication context.

Risk: The skill relies on SOCIALDATAX_API_KEY for access and may fail or expose billing context if the wrong key is configured.

Mitigation: Use the intended account key, keep it in the environment rather than in skill files, and verify the key when authentication or balance errors occur.

Risk: Douyin pagination uses opaque next_page_token values that can break result continuity if modified.

Mitigation: Preserve returned pagination tokens exactly when continuing the same search.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/douyin-trend-insights)
- [SocialDataX API key and product page](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-derived trend summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node, npm, and SOCIALDATAX_API_KEY; Douyin search results may include pagination tokens that should be preserved exactly when continuing a search.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
