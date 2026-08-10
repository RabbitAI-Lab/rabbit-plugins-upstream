## Description:

亚马逊全品类铺货与 Listing 选品专家。适用于跨类目铺货、批量发现商品机会、Listing 导向选品、全类目筛选和卖家精灵数据筛品的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to discover recently launched, fast-rising Amazon products across categories, export product lists, and optionally run preference-based ASIN scoring. It also supports scheduled product scouting when recurring scans are appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call LinkFox and SellerSprite APIs using the user's API key.

Mitigation: Install only in workspaces where API-key use for Amazon product scouting is approved, and review generated requests before running scripts that consume paid credits.

Risk: The bundle includes public file upload behavior.

Mitigation: Upload only files intended for public access, and avoid uploading sensitive, private, or proprietary material.

Risk: The bundle includes scheduled task creation.

Mitigation: Confirm scan frequency, marketplace, report format, notification settings, and credit cost before enabling recurring tasks.

Risk: The bundle includes tools that can modify other agents' CLAUDE.md files.

Mitigation: Use agent-instruction patching only after explicit review and confirmation that the target agent should be changed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-all-category-listing-scout)
- [SellerSprite product search API reference](skills/linkfox-sellersprite-product-search/references/api.md)
- [Product scout API parameter catalog](skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [ASIN scoring example expectations](skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [LinkFox task scheduler API reference](skills/linkfox-task-scheduler/references/api.md)
- [File upload API reference](skills/linkfox-file-upload/references/api.md)
- [AI text generation API reference](skills/linkfox-aigc-textgen/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and generated local files such as Excel, JSON, CSV, or HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary scouting outputs are Excel workbooks and concise Top 10 previews; supporting scripts may write JSON data, CSV-like tables, uploaded file URLs, scheduled task records, and report files.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
