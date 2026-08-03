## Description: <br>
Encrypt PDFs with AES-128, AES-256, or RC4 options and decrypt authorized PDFs with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document-processing teams use this skill to prepare ComPDF Server API requests for encrypting PDFs, setting document passwords and permissions, or decrypting PDFs after authorization is confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs and passwords may be sent to ComPDF for processing. <br>
Mitigation: Install only when this external processing is permitted, avoid highly sensitive documents unless approved, and use a dedicated private ComPDF API key file. <br>
Risk: PDF decryption can be misused if authorization is unclear. <br>
Mitigation: Require explicit user confirmation of authorization before decrypting and keep the agent constrained to the declared encrypt PDF and authorized decrypt PDF operations. <br>
Risk: API keys, passwords, and document contents are sensitive. <br>
Mitigation: Pass the API key only in the x-api-key header and do not place secrets or document contents in chat, logs, examples, or generated output. <br>


## Reference(s): <br>
- [ComPDF Skill Release Page](https://clawhub.ai/compdf-youna/skills/compdf-encryt-pdf-decrypt-pdf) <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF V2 API Overview](https://www.compdf.com/guides/api-reference/v2/api-overview) <br>
- [ComPDF V2 PDF API Overview](https://www.compdf.com/guides/api-reference/v2/api-overview-pdf) <br>
- [ComPDF V2 Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with endpoint details, request fields, expected response fields, and next-step instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not display API keys, passwords, or document contents; preserves original files unless replacement is explicitly requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
