## Description: <br>
云启智联AI服务 helps agents submit bank receipts, bank statements, invoices, and other financial documents to Yunqi Zhilian OCR services, retrieve asynchronous parse results, and generate accounting voucher drafts with confidence and review guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hinejon](https://clawhub.ai/user/hinejon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and finance teams use this skill to parse receipts, statements, invoices, and documents through Yunqi Zhilian OCR services and turn parsed results into accounting voucher drafts that a human accountant can review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial documents and related metadata may be uploaded to yunqi-zhilian.com for OCR. <br>
Mitigation: Use the skill only with documents the user explicitly intends to process through that service, and avoid triggering it for general finance discussion. <br>
Risk: Generated HTML and JSON outputs may contain sensitive financial data saved on the local machine. <br>
Mitigation: Store outputs in controlled locations and delete generated result or preview files when they are no longer needed. <br>
Risk: API keys can be provided on the command line or stored locally. <br>
Mitigation: Prefer environment-variable or managed secret injection and review local credential storage before use. <br>
Risk: OCR results and generated accounting vouchers may be incomplete or incorrectly classified. <br>
Mitigation: Have a qualified human review extracted fields, low-confidence matches, large transactions, and voucher entries before using them for accounting records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hinejon/skills/yqzl-ai-service) <br>
- [hinejon publisher profile](https://clawhub.ai/user/hinejon) <br>
- [Yunqi Zhilian website](https://www.yunqi-zhilian.com/) <br>
- [Yunqi Zhilian AI experience page](https://www.yunqi-zhilian.com/AIService/experience/page) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON or HTML file outputs from the bundled scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local JSON and HTML preview files for OCR results and voucher drafts.] <br>

## Skill Version(s): <br>
1.2.5 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
