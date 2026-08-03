## Description: <br>
Document OCR Agent helps agents send PDFs, images, or scanned documents to AgentPMT/Google Document AI to extract OCR text, structured entities, and per-page metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route document OCR and document intelligence requests through AgentPMT-hosted remote tool calls. It is suited for extracting text, receipt and invoice fields, tax form data, bank statement details, and per-page document metadata from supported files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted documents and extracted contents may be sent to AgentPMT/Google Document AI for processing. <br>
Mitigation: Use the skill only when third-party document processing is acceptable, and require explicit approval before sending IDs, tax forms, bank statements, medical or legal records, or similarly sensitive documents. <br>
Risk: Raw OCR responses can expose more document content and metadata than the agent needs. <br>
Mitigation: Keep include_raw_document disabled unless the full raw response is required, and scope inputs to exactly one source per request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/document-ocr-agent) <br>
- [AgentPMT marketplace product](https://www.agentpmt.com/marketplace/google-document-ai-ocr) <br>
- [Artifact skill instructions](artifact/SKILL.md) <br>
- [Artifact action schema](artifact/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [Markdown instructions with JSON tool-call examples and JSON OCR results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns extracted text excerpts, structured entities, optional page summaries, and optional raw Document AI response data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
