## Description: <br>
A Chinese-language insurance assistant for mainland China that helps with coverage planning, product comparison, premium estimates, protection-gap analysis, underwriting and compliance questions, claims topics, sales copy, and agent training scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China can use this skill to ask Chinese-language insurance planning questions, compare representative products, estimate premiums, and understand compliance or underwriting considerations. Insurance agents can use it to draft compliant customer-facing explanations, social posts, and training scripts. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: Insurance recommendations, premiums, policy terms, and availability may be preliminary or outdated. <br>
Mitigation: Verify product availability, premiums, and policy terms with an official insurer or licensed advisor before making decisions. <br>
Risk: The skill reads a large static product database that can include inactive, discontinued, or modified products. <br>
Mitigation: Use the product data as a screening aid and confirm high-value products against current official insurer materials. <br>
Risk: The skill may provide a specific sales-company contact when the user asks for contact help. <br>
Mitigation: Treat contact details as optional follow-up information, not an endorsement, and compare multiple licensed insurance sales or brokerage options. <br>
Risk: The skill provides insurance, compliance, and underwriting guidance that may be mistaken for licensed financial, legal, or insurance advice. <br>
Mitigation: Present outputs as preliminary information and escalate final decisions, legal questions, and policy purchases to licensed professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor) <br>
- [Publisher profile](https://clawhub.ai/user/mnetfairy) <br>
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md) <br>
- [Compliance reference](artifact/references/compliance.md) <br>
- [Product database](artifact/references/products.json) <br>
- [Product validation report](artifact/references/validation_report_20260524_090219.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Chinese-language Markdown responses with optional JSON produced by local Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include product-comparison tables, premium estimates, protection-gap reports, insurance-plan JSON, compliance reminders, and sales or training copy.] <br>

## Skill Version(s): <br>
1.8.418 (source: server release metadata; artifact frontmatter reports 1.8.351) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
