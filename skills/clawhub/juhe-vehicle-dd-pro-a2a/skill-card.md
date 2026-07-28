## Description: <br>
A Chinese-language paid vehicle due diligence skill that uses a VIN, vehicle type, and accident or illegal-modification status to request a Juhe vehicle report and return a structured pre-purchase Markdown summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and consumer agents use this skill for paid pre-purchase vehicle checks when they need a combined VIN configuration profile, registration fields, transfer history, and inspection-date estimate. It is intended for vehicle due diligence workflows, not standalone valuation, insurance, violation, theft, mortgage, or purchase-decision advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends a VIN, vehicle type, and accident or illegal-modification status to Juhe for a paid report through Alipay. <br>
Mitigation: Show the Chinese payment and privacy prompt before collection or payment, and proceed only after the user understands and confirms what will be queried. <br>
Risk: Vehicle report data could be misread as a valuation, insurance quote, violation report, or purchase recommendation. <br>
Mitigation: Keep the output limited to returned facts and the documented report sections; do not provide buy, do-not-buy, valuation, insurance, violation, theft, or mortgage conclusions. <br>
Risk: Returned registration data may include a vehicle plate value. <br>
Mitigation: Mask plate values in summaries, tables, follow-up answers, and logs according to the documented output rules. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/juhemcp/skills/juhe-vehicle-dd-pro-a2a) <br>
- [README.md](artifact/README.md) <br>
- [PRODUCT.md](artifact/PRODUCT.md) <br>
- [OUT_FORMAT.md](artifact/OUT_FORMAT.md) <br>
- [Juhe A2A Query Endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with structured tables, payment-flow prompts, and an inline HTTPS curl request template] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a valid VIN, mapped Chinese vehicle type, and accident or illegal-modification status; returned plate values must be masked before display.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
