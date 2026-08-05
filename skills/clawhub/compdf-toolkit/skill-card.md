## Description: <br>
All-in-one ComPDF workflow for document conversion, OCR, data extraction, PDF editing, protection, compression, and watermarking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document-workflow teams use this skill to select official ComPDF Server API endpoints and prepare request plans for conversion, OCR, structured extraction, page editing, protection, compression, watermarking, and related PDF workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documents may be uploaded to ComPDF's external service during user-directed processing. <br>
Mitigation: Use the skill only when ComPDF's service is intended for the workflow, and avoid regulated or highly confidential files unless ComPDF's data handling terms meet the user's requirements. <br>
Risk: Some supported operations can overwrite, delete, decrypt, or permanently protect documents. <br>
Mitigation: Identify affected files and obtain confirmation before those actions unless the user has already authorized them. <br>
Risk: API keys could be exposed if copied into prompts, code, logs, or examples. <br>
Mitigation: Read the key from the configured local file and pass it only in the x-api-key header. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](artifact/references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](artifact/references/official-api-reference.md) <br>
- [ComPDF V2 API Reference](https://www.compdf.com/guides/api-reference/v2/) <br>
- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/compdf-toolkit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with endpoint, method, content type, request fields, expected response fields, and follow-up polling or download steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not display API keys; asks for confirmation before overwrites, deletion, decryption, permanent protection, or external document upload when not already authorized.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
