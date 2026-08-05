## Description: <br>
Compress PDF files with ComPDF while balancing file size and readable visual quality. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to prepare ComPDF Server API requests that reduce PDF file size while preserving readable visual quality. It helps choose compression options, request fields, and follow-up steps for supported ComPDF compression workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs may be uploaded to ComPDF for processing. <br>
Mitigation: Use the skill only when the user is comfortable sending the document to ComPDF, and prefer documented asynchronous or presigned workflows for large, batch, or security-sensitive uploads. <br>
Risk: The skill relies on a local ComPDF API key file. <br>
Mitigation: Keep the API key file private, pass the key only in the x-api-key header, and do not include the key in code, logs, examples, or output. <br>
Risk: The bundled API snapshot includes unrelated ComPDF operations beyond compression. <br>
Mitigation: Restrict use to the documented compression endpoints and optimization flags, and avoid using unrelated decryption, editing, conversion, or AI extraction endpoints. <br>


## Reference(s): <br>
- [ComPDF Compress PDF skill page](https://clawhub.ai/compdf-youna/skills/compdf-compress-pdf) <br>
- [ComPDF endpoint index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API reference snapshot](references/official-api-reference.md) <br>
- [Official ComPDF compression guide](https://www.compdf.com/guides/api-reference/v2/compress-guides) <br>
- [Official ComPDF optimization flags](https://www.compdf.com/guides/api-reference/v2/optimization-flags) <br>
- [Official ComPDF authentication guide](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [Official ComPDF request workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown with endpoint details, request fields, and next-step instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include method, content type, task/result fields, polling steps, and download steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
