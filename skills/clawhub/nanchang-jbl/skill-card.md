## Description: <br>
Nanchang Jbl is a customer-service skill for Nanchang Carpoly paint and coating store inquiries, covering product guidance, promotions, after-sales policy, construction service information, and store navigation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liubuq-sys](https://clawhub.ai/user/liubuq-sys) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External customers and store support agents use this skill to answer paint, coating, renovation, waterproofing, promotion, after-sales, construction-service, and store-location questions for the Nanchang Carpoly merchant context. <br>

### Deployment Geography for Use: <br>
China (Nanchang, Jiangxi) <br>

## Known Risks and Mitigations: <br>
Risk: Broad home-improvement trigger words could activate this merchant-specific assistant in unrelated chats. <br>
Mitigation: Confirm the user wants Nanchang Carpoly merchant guidance before relying on store, pricing, promotion, or sales recommendations. <br>
Risk: Prices, promotions, inventory, and service availability can change. <br>
Mitigation: Treat those answers as reference guidance and direct users to confirm final details with the relevant store. <br>
Risk: The skill cannot complete operational actions such as refunds, after-sales processing, construction scheduling, or service appointments. <br>
Mitigation: Route operational requests to the listed store phone or in-store staff instead of promising to arrange or execute the action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liubuq-sys/skills/nanchang-jbl) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Business and store basics](references/business-info.md) <br>
- [Product information](references/services.md) <br>
- [Recommendation logic](references/recommendations.md) <br>
- [Promotions and membership](references/promotions.md) <br>
- [After-sales policy](references/after-sales.md) <br>
- [Construction service information](references/construction.md) <br>
- [Store directory](references/stores.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain-language conversational responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should be grounded in the bundled reference files and should treat prices, promotions, and service availability as store-confirmed information.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
