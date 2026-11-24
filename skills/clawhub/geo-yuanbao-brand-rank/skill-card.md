## Description:

查询腾讯元宝对指定品牌的推荐、排名、同现竞品和引用网页，并生成可分享的结果报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[hclscut](https://clawhub.ai/user/hclscut)

### License/Terms of Use:

MIT-0

## Use Case:

品牌经营者和营销团队可用它检查腾讯元宝在具体推荐问题中是否提及某个品牌、品牌出现的位置、同场竞品及引用来源，并据此规划内容改进。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A small set of AI responses may be presented as a definitive brand recommendation or ranking, although results can vary by prompt and run.

Mitigation: Describe findings as observations from the specific queried prompts, distinguish reputation questions from ranking questions, and repeat the same questions across separate days before drawing stability conclusions.

Risk: The skill's Yuanbao-focused description can be confused with its broader platform options.

Mitigation: Identify the platform queried in each report and limit conclusions to the platforms actually selected.

Risk: Sharing a paid API key in chat can expose the credential.

Mitigation: Keep the key in an approved local secret store or environment variable; do not send or repeat it in chat.

## Reference(s):

- [MaxAEO Developer API Documentation](https://maxaeo.cn/docs/developers/)

## Skill Output:

**Output Type(s):** [Text, HTML report, Guidance]

**Output Format:** [Text summary and shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes observed brand mentions, reported positions, competitors, and cited websites for the queried prompts.]

## Skill Version(s):

1.0.0 (source: frontmatter; server release version 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
