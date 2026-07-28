## Description: <br>
PRICE() helps agents evaluate quotation strategy and negotiable boundaries from purchase quotes, customer value, quantity, condition, delivery timing, payment terms, and risk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ClawHub users can use this skill to structure RFQ and quotation analysis before proposing a pricing strategy. The skill is intended to surface required inputs, risk factors, negotiable space, suggested quote structure, and items needing human confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may include confidential pricing, customer, or margin information in prompts. <br>
Mitigation: Avoid entering unnecessary confidential pricing or customer data unless it is appropriate for the workspace. <br>
Risk: The current artifact is Chinese-language and marked draft for testing, which may limit multilingual or production-ready use. <br>
Mitigation: Review and adapt the skill before relying on it for multilingual workflows or production quotation processes. <br>
Risk: Incomplete quotation inputs can lead to misleading or overly precise pricing recommendations. <br>
Mitigation: Use the skill's required parameter checks and keep outputs in preliminary-analysis mode until missing, conflicting, or unverified inputs are resolved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-price) <br>
- [Publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown analysis with tables and structured pricing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language output expected from the current artifact; no tool execution, persistence, or data-transfer behavior is described.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
