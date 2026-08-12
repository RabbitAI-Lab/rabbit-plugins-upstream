## Description:

Searches GeekBI Temu product data to help sellers find and compare products by keyword, category, site, sales, revenue, price, supply price, similar-product count, ratings, listing age, and trend signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and commerce analysts use this skill to research Temu product opportunities, compare candidates, assess pricing and competition, and decide what to validate next using GeekBI-returned product data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Python scripts and contacts GeekBI APIs to retrieve Temu product data.

Mitigation: Install and run it only in environments where outbound GeekBI API access and local script execution are approved.

Risk: The skill can reuse or store GeekBI login state in .geekbi/agent-auth.json locations.

Mitigation: Use only trusted GeekBI accounts, protect the local login-state file, and remove stored state when access should end.

Risk: Business conclusions depend on the returned data scope, pagination, filters, and update time.

Mitigation: Review the stated data scope and require additional pages or refreshed queries before making high-impact sourcing decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-product-search-skill)
- [Server-resolved source repository](https://github.com/geekbi/geekbi-temu-product-search-skill)
- [GeekBI API endpoint](https://openapi.geekbi.com)
- [Temu 商品搜索](references/Temu商品搜索.md)
- [Temu 商品搜索接口](references/Temu商品搜索接口.md)
- [Temu 商品榜单查询预设](references/Temu商品榜单预设.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown analysis with product links, concise findings, data scope, risks, and recommended next actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run local Python helper scripts that return JSON from GeekBI APIs before presenting user-facing analysis.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
