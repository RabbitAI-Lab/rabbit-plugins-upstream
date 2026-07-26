## Description: <br>
将单份 DRG 或 DIP 目录的 XLSX、PDF、扫描/OCR PDF 或 DOCX 原始材料整理为可检索交互报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[u201013903](https://clawhub.ai/user/u201013903) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Healthcare catalogue analysts and governance teams use this skill to process one DRG or DIP source catalogue, validate extracted rows, resolve review items, and receive a quality summary with an interactive report link. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uploads user-provided DRG/DIP catalogue source files to the MedGroup catalogue-report service. <br>
Mitigation: Use it only for intended catalogue files and avoid unrelated confidential documents. <br>
Risk: MedGroup API keys could be exposed if placed in prompts, reports, or shared files. <br>
Mitigation: Keep the API key in client MCP configuration and do not include it in skill outputs or uploaded report materials. <br>
Risk: OCR or scanned source files can contain uncertain codes, values, or column alignment. <br>
Mitigation: Use field confidence, validation, and the review protocol before treating the report as complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/u201013903/skills/mfz-catalogue-report) <br>
- [Exchange contract](references/exchange-contract.md) <br>
- [Review protocol](references/review-protocol.md) <br>
- [MedGroup Catalogue Report MCP](https://medgroup.medchat.fun/catalogue-report/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown status updates with quality summary, warnings, and report URL] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create temporary NDJSON or conversion scripts during processing, but final user-facing output is limited to status, quality summary, warnings, and report link.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
