## Description:

当用户需要做小红书趋势洞察、小红书趋势分析、热点观察、内容方向判断、趋势线索归纳或营销灵感整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand researchers, and creators use this skill to inspect Xiaohongshu/XHS hot-search and keyword-search results, then summarize ranking signals, sample posts, audience feedback, creator positioning, topic patterns, and next analysis angles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SocialDataX CLI receives SOCIALDATAX_API_KEY for read-only XHS data calls.

Mitigation: Use a scoped key where available, store it only in the runtime environment, and avoid writing it into prompts, files, shell history, or generated skill content.

Risk: Returned XHS note URLs may include xsec_token values that behave like sensitive links.

Mitigation: Preserve full URLs when traceability is required, but share them only with recipients who need access to the specific analysis evidence.

Risk: Paginated search results and recent-topic filters may cover only the retrieved pages rather than the whole platform.

Mitigation: State the query, sorting, time window, page count, and any pagination limits when summarizing trend conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-trend-insights-v2)
- [SocialDataX API key and product page](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with CLI command examples and structured trend observations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ranking and heat signals, related titles, author or account names, content IDs, original XHS note URLs, and suggested follow-up questions.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
