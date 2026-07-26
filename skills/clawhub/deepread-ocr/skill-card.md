## Description: <br>
DeepRead OCR helps agents process PDFs and images through the DeepRead API to extract markdown text, structured JSON fields, confidence signals, and human-review flags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[uday390](https://clawhub.ai/user/uday390) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to integrate DeepRead document OCR into invoice, receipt, contract, form digitization, and document workflow automation. The skill guides agents through API-key setup, document upload, webhook or polling flows, schema-based extraction, confidence flags, and human-in-the-loop review handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded documents, extracted data, preview URLs, webhooks, and BYOK provider calls can involve sensitive external data sharing. <br>
Mitigation: Use the skill only when external processing is allowed by policy, secure webhook receivers, choose approved BYOK providers, and treat preview URLs as private links. <br>
Risk: The DEEPREAD_API_KEY can grant account access if exposed in files, chats, logs, or shared configuration. <br>
Mitigation: Store the key in the environment, avoid hardcoding it, keep it out of prompts and logs, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [DeepRead Homepage](https://www.deepread.tech) <br>
- [DeepRead Dashboard](https://www.deepread.tech/dashboard) <br>
- [DeepRead BYOK Setup](https://www.deepread.tech/dashboard/byok) <br>
- [ClawHub DeepRead OCR Skill](https://clawhub.ai/uday390/skills/deepread-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON examples, configuration snippets, and API response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DEEPREAD_API_KEY and may reference webhook endpoints, preview URLs, schemas, blueprints, and BYOK provider configuration.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
