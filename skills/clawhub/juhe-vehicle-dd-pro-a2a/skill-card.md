## Description: <br>
车辆尽调报告 Pro（标准版）通过一次付费 VIN 查询生成车辆配置、登记五项、过户流转和车检估算的购前快检报告，并在付款前要求确认车辆类型与事故/非法改装情况。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and purchasing agents use this skill to run a paid VIN-based pre-purchase vehicle check that combines configuration, registration, transfer history, and inspection-estimate details into a structured report. It is intended for second-hand vehicle due diligence, model and ownership-flow checks, and basic financial or insurance review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends VIN, vehicle type, and accident or illegal-modification status to Juhe as part of a paid query. <br>
Mitigation: Show the privacy and payment notice before collection, collect only the required fields, and let the user cancel before any paid request is made. <br>
Risk: Returned vehicle identifiers or payment details could expose sensitive information if shown verbatim. <br>
Mitigation: Mask vehicle plates in reports and avoid logging full VINs, full plates, raw query text, or complete payment response details. <br>
Risk: Invalid or incomplete vehicle inputs could trigger a paid query with incorrect or empty results. <br>
Mitigation: Validate the VIN format and collect explicit vehicle type and accident/illegal-modification answers before starting the payment flow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/juhemcp/skills/juhe-vehicle-dd-pro-a2a) <br>
- [Publisher Profile](https://clawhub.ai/user/juhemcp) <br>
- [README](artifact/README.md) <br>
- [Output Format](artifact/OUT_FORMAT.md) <br>
- [Product Lock](artifact/PRODUCT.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with structured tables, concise user guidance, and payment/request command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a valid VIN, vehicle type, accident/illegal-modification answer, and Alipay payment confirmation; returned vehicle plates must be masked.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
