## Description:

证券指数信息与行情查询技能，用于把中文自然语言中的指数查询请求转成真实数据查询，并返回指数基础信息、分类、成分股、收益风险、估值基本面、相关基金和行情信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[e-fintech](https://clawhub.ai/user/e-fintech)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query and compare Chinese securities indexes, including constituents, valuation, fundamentals, performance, related funds, and market quotes. It is intended for factual information retrieval and comparison, not investment advice or trading decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses an Index Hub API key locally and sends index query requests to www.etf.com.cn.

Mitigation: Install only after trusting the provider, protect ~/.config/index-hub/api_key, and prefer the documented INDEX_HUB_API_KEY override for temporary credentials.

Risk: Installer execution may replace an existing index-query skill in the selected skills directory.

Mitigation: Use --skills-dir for an isolated install location when preserving another installation matters.

Risk: Market data answers could be mistaken for investment advice or future-performance predictions.

Mitigation: Keep responses factual, include dates or quote times, preserve the provider disclaimer, and use the bundled answer guardrails before final output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/e-fintech/skills/index-query)
- [Index Hub help document](https://cdn.efunds.com.cn/eda/h5/itcenter/pd/ai-skills-doc/help.pdf)
- [Index query catalog](references/catalog-index.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with concise tables or lists and occasional shell commands for setup or troubleshooting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final answers should include data dates or quote times, avoid raw responses and credentials, and retain the provider disclaimer.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence; artifact frontmatter reports metadata.version 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
