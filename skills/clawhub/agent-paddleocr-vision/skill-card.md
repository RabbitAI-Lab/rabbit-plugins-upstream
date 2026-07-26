## Description: <br>
Multi-language document understanding with PaddleOCR. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nhzallen](https://clawhub.ai/user/nhzallen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to process documents through a configured PaddleOCR cloud API, extract OCR and document-type information, suggest actions, batch process files, and optionally generate searchable PDFs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Processed documents may be uploaded to a configured PaddleOCR cloud service, including sensitive IDs, passports, bank records, tax forms, and contracts. <br>
Mitigation: Confirm authorization to use the configured service for the document types being processed and follow organizational data handling rules before uploading files. <br>
Risk: The release artifact references external repository scripts and documentation that are not included in the artifact. <br>
Mitigation: Review the referenced repository files, dependency list, and runtime commands before installing dependencies or running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nhzallen/skills/agent-paddleocr-vision) <br>
- [Server-resolved GitHub provenance](https://github.com/NHZallen/agent-paddleocr-vision) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and references to OCR JSON and searchable PDF outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a PaddleOCR document parsing API URL and access token; processed documents are sent to the configured PaddleOCR cloud service.] <br>

## Skill Version(s): <br>
1.1.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
