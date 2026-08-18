## Description:

通过极鲸云提供的 SHEIN 商品、图搜同款、店铺、类目、关键词和评论数据，帮助跨境电商用户完成选品、竞品分析、需求趋势判断、价格带分析、竞争强度评估、用户痛点提炼和市场调研。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, market researchers, and product-selection analysts use this skill to query GeekBI's SHEIN data and turn product, image, shop, category, keyword, and review results into concise market research guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided images or URLs may be sent to GeekBI during image-based SHEIN market research without sufficiently prominent consent language.

Mitigation: Confirm user intent before image or URL analysis, avoid confidential or private-network content, and add clear privacy and consent language before deployment.

Risk: GeekBI login state is stored under a mismatched Temu namespace, which can create confusion about credential scope and storage.

Mitigation: Review and correct the authentication storage namespace before organizational rollout, then retest login and logout behavior.

Risk: The server security verdict is suspicious even though no individual risk findings were listed.

Mitigation: Require human review of the Clawscan summary and guidance before installation in sensitive or managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-shein-research-skill)
- [Publisher profile](https://clawhub.ai/user/geekbi)
- [Server-resolved GitHub source](https://github.com/geekbi/geekbi-shein-research-skill)
- [接口总览](references/接口总览.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [SHEIN商品搜索](references/SHEIN商品搜索.md)
- [SHEIN图搜同款](references/SHEIN图搜同款.md)
- [SHEIN店铺搜索](references/SHEIN店铺搜索.md)
- [SHEIN类目搜索](references/SHEIN类目搜索.md)
- [SHEIN关键词搜索](references/SHEIN关键词搜索.md)
- [SHEIN评论搜索](references/SHEIN评论搜索.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with Chinese market research summaries, linked result names, tables, data caveats, opportunity notes, risk notes, and recommended next actions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish API facts, recalculable metrics, and analysis judgments, and should preserve site, currency, time range, filters, pagination, sample size, and data update context when available.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
