## Description: <br>
Temu US promotion API helper for querying promotion activities, finding candidate goods, enrolling goods, checking promotion operations, and updating enrolled promotion goods through LinkFox. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and ecommerce operators use this skill to prepare and run Temu US promotion workflows, including promotion activity lookup, candidate goods review, goods enrollment, operation-result checks, and enrolled-goods updates. <br>

### Deployment Geography for Use: <br>
Global, for Temu US marketplace workflows. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make broad Temu API calls through the LinkFox gateway. <br>
Mitigation: Restrict use to documented promotion endpoints and review the request type and payload before execution. <br>
Risk: Temu access tokens may be handled or stored in plaintext. <br>
Mitigation: Avoid saving tokens in plaintext when possible, protect any token store, and never commit tokens to source control. <br>
Risk: Saved API responses may contain business or account data. <br>
Mitigation: Treat saved response files as sensitive, keep them out of version control, and delete or redact them when no longer needed. <br>
Risk: Goods enrollment, update, or deactivation calls can affect live promotion operations. <br>
Mitigation: Require explicit review before business-impacting API calls and confirm the target activity, goods, SKU, price, quantity, and operation type. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-promotion-us) <br>
- [API reference](references/api.md) <br>
- [Temu accessToken authorization and retrieval](references/access-token.md) <br>
- [Partner US Promotion API catalog](references/partner-us-catalog.md) <br>
- [Promotion endpoint documentation index](references/apis/README.md) <br>
- [bg.promotion.activity.query](references/apis/bg-promotion-activity-query.md) <br>
- [bg.promotion.activity.candidate.goods.query](references/apis/bg-promotion-activity-candidate-goods-query.md) <br>
- [bg.promotion.activity.goods.query](references/apis/bg-promotion-activity-goods-query.md) <br>
- [bg.promotion.activity.goods.enroll](references/apis/bg-promotion-activity-goods-enroll.md) <br>
- [bg.promotion.activity.goods.operation.query](references/apis/bg-promotion-activity-goods-operation-query.md) <br>
- [bg.promotion.activity.goods.update](references/apis/bg-promotion-activity-goods-update.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts may save full API responses locally and print full JSON or summaries depending on response size.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
