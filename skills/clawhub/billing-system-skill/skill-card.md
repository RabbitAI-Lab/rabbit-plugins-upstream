## Description: <br>
Generates billing reconciliation statements from spreadsheet inputs, using either an online Tencent SCF workflow or a local Windows EXE workflow to produce Excel summaries and monthly customer PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nihao-ok](https://clawhub.ai/user/nihao-ok) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to prepare customer, loan, and repayment spreadsheets and generate reconciliation outputs. It supports billing operations that can choose between cloud generation and a local Windows executable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer billing, loan, repayment, and balance spreadsheets may be uploaded to an external Tencent SCF service. <br>
Mitigation: Confirm the destination URL and get explicit user approval before any upload; use the local/offline workflow for sensitive records unless the service operator and data handling practices are trusted. <br>
Risk: The online workflow uses an auto-registered trial key and a quota-based paid account model. <br>
Mitigation: Confirm account, key storage, and quota expectations before generation, and stop for user approval if the service returns a payment or quota error. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nihao-ok/skills/billing-system-skill) <br>
- [Server-resolved source repository](https://github.com/nihao-ok/billing-system-skill) <br>
- [Tencent SCF service endpoint](https://1440636612-55rmw631p6.ap-beijing.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with bash and Python examples; generated artifacts are Excel, PDF, and ZIP files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The online workflow can upload spreadsheet data to an external cloud service; the local Windows EXE workflow is described as offline.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
