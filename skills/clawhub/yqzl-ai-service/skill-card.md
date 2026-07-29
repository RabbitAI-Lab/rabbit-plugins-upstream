## Description: <br>
Yunqi Zhilian AI Service helps agents submit financial documents to Yunqi Zhilian OCR APIs, retrieve asynchronous parsing results, and generate local accounting vouchers with confidence scores and review suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hinejon](https://clawhub.ai/user/hinejon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and finance operations users use this skill to parse bank receipts, bank statements, invoices, and general documents, then present OCR results or accounting voucher drafts for human review. It supports trial usage without an API key and configured API-key usage for normal service access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial documents and OCR inputs may be sent to a third-party service. <br>
Mitigation: Install and use only if the publisher is trusted and the documents are approved for processing by Yunqi Zhilian. <br>
Risk: The skill can automatically download and replace its installed code without user approval or package integrity verification. <br>
Mitigation: Review or disable the automatic updater before use, and avoid environment or CLI overrides of the update URL. <br>
Risk: Generated HTML and JSON preview files can contain sensitive financial records. <br>
Mitigation: Store, share, and delete generated preview files according to the user's sensitive-data handling requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hinejon/skills/yqzl-ai-service) <br>
- [Yunqi Zhilian AI Service](https://www.yunqi-zhilian.com/AIService) <br>
- [Yunqi Zhilian AI experience page](https://www.yunqi-zhilian.com/AIService/experience/page) <br>
- [Yunqi Zhilian website](https://www.yunqi-zhilian.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, API calls, JSON, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON API results, and generated HTML or JSON preview files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local OCR preview HTML, voucher JSON, and voucher HTML files containing financial data.] <br>

## Skill Version(s): <br>
1.2.4 (source: frontmatter, artifact/version, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
