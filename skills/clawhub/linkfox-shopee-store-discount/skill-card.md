## Description: <br>
Shopee-店铺折扣 helps agents create, list, update, end, and delete Shopee store discount promotions through LinkFox's Shopee developer proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to manage authorized Shopee store discount campaigns, including creating promotions, adding or updating items, ending promotions, and reviewing discount details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, end, and delete live Shopee store discount promotions. <br>
Mitigation: Require explicit user confirmation before any create, update, end, or delete action and review request parameters before execution. <br>
Risk: Full LinkFox and Shopee API responses may be saved locally and can contain sensitive merchant data. <br>
Mitigation: Treat saved response files as sensitive, keep them in an appropriate workspace, and review or delete them after use. <br>


## Reference(s): <br>
- [API reference](references/api.md) <br>
- [Shopee Open Platform Discount API](https://open.shopee.com/documents/v2/v2.discount.add_discount?module=99&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, JSON, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON response output or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved under a local linkfox data directory; small responses print full JSON and larger responses print summaries unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
