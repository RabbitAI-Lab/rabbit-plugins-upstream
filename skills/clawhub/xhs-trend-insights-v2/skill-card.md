## Description:

当用户需要做小红书趋势洞察、小红书趋势分析、热点观察、内容方向判断、趋势线索归纳或营销灵感整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand researchers, and creators use this skill to review Xiaohongshu trends and hot topics, assess content directions, and collect marketing ideas from trend and search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX and may contain sensitive context.

Mitigation: Avoid confidential details in search terms; use focused, non-sensitive queries.

Risk: Requests may consume paid SocialDataX credits.

Mitigation: Start with one page or a small item limit, then expand only when needed.

Risk: The external CLI package's runtime behavior is outside this artifact review.

Mitigation: Use a reviewed, fixed CLI version when making direct CLI calls.

Risk: The API key is a secret credential that should remain private.

Mitigation: Store it in the execution environment's supported secret storage and never include it in chat, logs, screenshots, or skill files.

## Reference(s):

- [SocialDataX AI and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/xhs-trend-insights-v2)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown summaries of trend rankings and signals, sample titles, authors, links or IDs, and follow-up research angles.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only trend research; results reflect the returned samples and ranking signals.]

## Skill Version(s):

0.1.6 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
