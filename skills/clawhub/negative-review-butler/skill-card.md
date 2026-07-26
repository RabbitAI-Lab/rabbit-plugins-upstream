## Description: <br>
差评管家 helps Chinese merchants batch process store reviews, classify complaint causes and severity, flag high-risk cases, and draft personalized public replies for human review before posting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenobiazizi](https://clawhub.ai/user/zenobiazizi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Chinese-language restaurant, local-services, and e-commerce merchants use this skill to turn pasted, screenshot, or exported review batches into categorized complaint summaries, severity labels, suggested remediation, and reply drafts for manual approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer review batches can include personal or sensitive customer information. <br>
Mitigation: Review and minimize customer data before sharing it with the agent; keep phone numbers and other personal details masked in outputs. <br>
Risk: Draft public replies may be inaccurate or unsuitable for safety, legal, refund, or serious complaint cases. <br>
Mitigation: Manually review every draft before posting and handle high-risk complaints through direct contact or internal escalation before publishing a response. <br>
Risk: The workflow is optimized for Chinese merchant review scenarios and may be less reliable outside that language or context. <br>
Mitigation: Use it primarily for Chinese review workflows and verify classifications, tone, and remediation advice when applying it to other contexts. <br>


## Reference(s): <br>
- [餐饮 / 本地生活行业模板](artifact/references/template-dining.md) <br>
- [电商行业模板](artifact/references/template-ecom.md) <br>
- [输出效果示例](artifact/examples/sample-output.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown review-reply table with summaries, severity labels, draft replies, and remediation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Drafts are intended for manual review and public posting by the user; high-risk safety, legal, refund, or complaint cases require extra human checks.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
