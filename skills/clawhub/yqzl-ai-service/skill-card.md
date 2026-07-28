## Description: <br>
Yunqi Zhilian AI Service helps agents submit financial documents for OCR parsing, query asynchronous results, and generate accounting voucher drafts with confidence and review guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hinejon](https://clawhub.ai/user/hinejon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and accounting-oriented agents use this skill to parse bank receipts, bank statements, invoices, and general files through Yunqi Zhilian services, then present OCR results or accounting voucher drafts for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically replace its own code from a remote ZIP. <br>
Mitigation: Review or disable automatic self-update behavior unless updates are signed, verified, and explicitly approved. <br>
Risk: Financial documents or file URLs are sent to yunqi-zhilian.com for parsing. <br>
Mitigation: Use only with documents approved for that service and follow the organization's data handling requirements before upload. <br>
Risk: Parsed financial outputs and voucher files may be saved locally as HTML or JSON. <br>
Mitigation: Store generated files in controlled locations, restrict access, and delete or archive them according to retention policy. <br>
Risk: Generated accounting vouchers are draft classifications with confidence scores and review suggestions. <br>
Mitigation: Have qualified personnel review account mappings, amounts, and low-confidence or high-value transactions before posting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hinejon/skills/yqzl-ai-service) <br>
- [Yunqi Zhilian website](https://www.yunqi-zhilian.com/) <br>
- [Yunqi Zhilian AI experience page](https://www.yunqi-zhilian.com/AIService/experience/page) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, HTML files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON API results, and optional generated HTML or JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Financial parsing calls may return asynchronous task identifiers; voucher outputs include accounting entries, confidence scores, and review suggestions.] <br>

## Skill Version(s): <br>
1.2.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
