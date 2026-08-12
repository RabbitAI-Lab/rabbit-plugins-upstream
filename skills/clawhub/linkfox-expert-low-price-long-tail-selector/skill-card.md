## Description:

亚马逊低价长尾选品专家。适用于寻找低价长尾商品、低价细分关键词机会、低竞争长尾产品想法，以及按长尾需求和价格筛选商品的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this skill to find low-price, low-competition long-tail product opportunities, export candidates, and optionally score ASINs against seller preferences. The workflow can also schedule recurring product-scouting runs after user confirmation.

### Deployment Geography for Use:

Global; the artifact states support for US, UK, DE, FR, JP, CA, IT, ES, MX, and IN Amazon marketplaces.

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API credentials and may consume paid credits or create billing orders.

Mitigation: Confirm account, quota, and expected credit cost before running product search, AIGC, scheduling, or payment-related flows.

Risk: The bundled file-upload capability can publish selected local files to publicly accessible URLs.

Mitigation: Upload only files intended for public sharing and review generated URLs before distributing them or passing them to downstream services.

Risk: The scheduling capability can create recurring automated agent tasks.

Mitigation: Require explicit confirmation of schedule, parameters, notifications, and expected daily credit use before enabling recurring runs.

Risk: A bundled helper script can modify other agent instruction files if executed.

Mitigation: Review file targets and diffs before running instruction-modification scripts, and run them only in a controlled workspace.

Risk: The package stores generated outputs and workflow state locally.

Mitigation: Use an appropriate workspace for account-linked outputs and remove local artifacts that contain sensitive marketplace or credential-adjacent data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-low-price-long-tail-selector)
- [Product Scout API Parameters Catalog](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [SellerSprite Product Search API](artifact/skills/linkfox-sellersprite-product-search/references/api.md)
- [ASIN Dynamic Scoring Example Expectations](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [Task Scheduler API](artifact/skills/linkfox-task-scheduler/references/api.md)
- [File Upload API](artifact/skills/linkfox-file-upload/references/api.md)
- [AIGC Text Generation API](artifact/skills/linkfox-aigc-textgen/references/api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Files]

**Output Format:** [Markdown instructions and tables, shell command invocations, JSON status payloads, and Excel or CSV files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product-scouting runs produce files such as scout_round{N}_new_products.xlsx, scout_all_unique_products.xlsx, and scoring_result.xlsx; LinkFox API credentials and credits may be required.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
