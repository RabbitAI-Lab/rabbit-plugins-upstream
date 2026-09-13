## Description:

使用极鲸云查询 Shopee 类目列表、类目父链和可信类目 ID，并结合类目下商品样本研究销量、销售额、价格带、供给结构和品类机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and ecommerce operators use this skill to identify Shopee category paths, verify category IDs, and study product samples for category selection and competitive research. It is intended for bounded sample analysis, not official platform-wide market sizing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication state may be stored as plaintext in more than one local directory.

Mitigation: Install only in trusted environments, limit local filesystem access to the agent workspace and user config paths, and remove stored GeekBI authentication state when the skill is no longer needed.

Risk: Custom API or authentication base URLs could direct requests to untrusted endpoints.

Mitigation: Use the documented GeekBI endpoint by default and review any request to override --base-url before execution.

Risk: Server-provided login links require user action and could be mishandled.

Mitigation: Show only the server-provided message and jumpUrl, verify the destination before opening it, and do not expose tokens, device codes, request headers, or internal authentication objects.

Risk: Shopee product samples are capped and do not represent full market size or official GMV.

Mitigation: Report filters, sample size, total-result cap, site, and update time, and validate compliance and marketplace requirements in the target Seller Centre before acting.

## Reference(s):

- [Server-resolved GitHub import](https://github.com/geekbi/geekbi-shopee-category-search-skill)
- [Shopee 类目接口](references/Shopee类目接口.md)
- [Shopee 类目研究](references/Shopee类目研究.md)
- [Shopee 运营与政策口径](references/Shopee运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [GeekBI OpenAPI](https://openapi.geekbi.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown summaries with JSON command outputs when scripts are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state filters, sample size, total-result cap, site, and update time when reporting Shopee product samples.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
