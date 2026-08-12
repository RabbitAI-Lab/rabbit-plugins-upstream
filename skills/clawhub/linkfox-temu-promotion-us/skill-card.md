## Description:

Temu 美国站电商促销 API，经 LinkFox 网关转发 Partner US Promotion / 促销活动相关 bg/temu 接口，用于活动创建、报名、查询、优惠券和秒杀等促销工作流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to query Temu US promotion activities, inspect candidate goods, enroll goods, check operation results, and update enrolled promotion goods through LinkFox and Temu credentials.

### Deployment Geography for Use:

Global, for Temu US and Partner US promotion workflows.

## Known Risks and Mitigations:

Risk: The skill requires LinkFox and Temu credential access.

Mitigation: Use least-privilege tokens, avoid unmasking or printing tokens, and review saved token files under ~/.linkfox.

Risk: The skill can proxy promotion actions such as enrollment, updates, file downloads, and billing or onboarding flows.

Mitigation: Require explicit user confirmation before promotion-changing, payment, onboarding, or file-download commands.

Risk: The skill writes local response archives that may contain marketplace or promotion data.

Mitigation: Review files saved under linkfox/ before sharing logs or committing workspace contents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-promotion-us)
- [linkfox-temu-promotion-us API reference](references/api.md)
- [Temu accessToken authorization and retrieval](references/access-token.md)
- [Temu authorization flow](references/authorization-flow.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Partner US Promotion interface catalog](references/partner-us-catalog.md)
- [Promotion API documentation index](references/apis/README.md)
- [Promotion activity query](references/apis/bg-promotion-activity-query.md)
- [Promotion candidate goods query](references/apis/bg-promotion-activity-candidate-goods-query.md)
- [Promotion enrolled goods query](references/apis/bg-promotion-activity-goods-query.md)
- [Promotion goods enrollment](references/apis/bg-promotion-activity-goods-enroll.md)
- [Promotion goods operation query](references/apis/bg-promotion-activity-goods-operation-query.md)
- [Promotion goods update](references/apis/bg-promotion-activity-goods-update.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON files]

**Output Format:** [Markdown guidance with shell command examples and JSON request or response payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under linkfox/ session folders; small responses may also print complete JSON to stdout, while larger responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
