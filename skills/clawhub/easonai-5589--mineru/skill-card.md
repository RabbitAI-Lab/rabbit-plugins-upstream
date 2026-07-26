## Description: <br>
Uses the MinerU API to parse PDF, Word, PowerPoint, and image files into Markdown with support for formulas, tables, and OCR. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[easonai-5589](https://clawhub.ai/user/easonai-5589) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and document-processing agents use this skill to submit documents to MinerU and retrieve structured Markdown for paper reading, extraction, OCR, formula recognition, and table parsing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Document URLs or uploaded files are sent to MinerU for cloud processing. <br>
Mitigation: Use only approved documents and review MinerU's privacy and retention terms before processing confidential, regulated, or proprietary material. <br>
Risk: The MINERU_TOKEN credential can be exposed through shared logs, repositories, terminal history, or screenshots. <br>
Mitigation: Store the token in a local secret store or environment variable, avoid printing it, and rotate it if exposure is suspected. <br>
Risk: Very large documents may exceed the documented 200 MB or 600 page limits. <br>
Mitigation: Check file size and page count before submission, split large documents, or use batch workflows within the plan's concurrency limits. <br>


## Reference(s): <br>
- [MinerU website](https://mineru.net/) <br>
- [MinerU API documentation](https://mineru.net/apiManage/docs) <br>
- [MinerU GitHub repository](https://github.com/opendatalab/MinerU) <br>
- [ClawHub skill page](https://clawhub.ai/easonai-5589/skills/mineru) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline bash, curl, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents through cloud document parsing; MinerU results may include Markdown, structured JSON, extracted images, and layout data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
