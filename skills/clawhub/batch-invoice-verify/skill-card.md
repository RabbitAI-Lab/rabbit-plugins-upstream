## Description: <br>
面向企业财务场景的发票批处理 AI 助手，用于批量发票识别、真伪核验、重复报销风险识别及台账生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ningmengyun12366](https://clawhub.ai/user/ningmengyun12366) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance teams and business users use this skill to process batches of invoice files, verify invoice authenticity, identify duplicate reimbursement risk, and generate standardized invoice ledger output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that the skill fetches and runs remotely downloaded software. <br>
Mitigation: Review the skill before installing, trust the publisher and download host before use, and prefer releases that verify downloaded binaries with signed hashes. <br>
Risk: The security evidence reports that the workflow handles an invoice API key through chat. <br>
Mitigation: Provide the API key through a secure workflow, avoid long-lived credentials, and do not store the key in configuration, logs, cache, or output files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ningmengyun12366/skills/batch-invoice-verify) <br>
- [Publisher profile](https://clawhub.ai/user/ningmengyun12366) <br>
- [Installation and update guide](https://download.ningmengyun.com/Skills/batch-invoice-verify/batch-invoice-verify-install.md) <br>
- [Ningmengyun AI tax platform](https://www.nmy.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce XLSX file paths and invoice-processing statistics through the workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and changelog; artifact frontmatter states 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
