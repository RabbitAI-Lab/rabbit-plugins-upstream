## Description: <br>
综合市场需求、客户询价、我方供应优势、采购难度、资金占用、利润、价格波动、物流、认证和售后风险，对候选产品进行市场机会与进入评估，并输出优先验证、小范围试销、持续观察、暂不进入或信息不足；不等同热门产品推荐。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product, procurement, sales, and operations teams use this skill to compare candidate products against market demand, customer inquiries, supplier fit, capital constraints, margin potential, logistics, certification, and after-sales risk. It helps classify each candidate as priority validation, small-scale trial sale, continued observation, do not enter, or insufficient information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may receive commercially sensitive supplier terms, margins, budgets, inventory plans, customer inquiries, or after-sales information. <br>
Mitigation: Provide only data approved for the agent context, and redact or summarize sensitive commercial inputs where possible. <br>
Risk: Incomplete or unreliable market, sales, pricing, or margin evidence could lead to misleading product-entry recommendations. <br>
Mitigation: Keep the skill's evidence and gap reporting visible, avoid invented figures, and treat validation or trial-sale recommendations as bounded next steps rather than bulk stocking decisions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or structured text with product comparison tables, evidence notes, gaps, validation actions, and stop conditions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable code, persistence, credential use, or external tool calls are described in the release evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
