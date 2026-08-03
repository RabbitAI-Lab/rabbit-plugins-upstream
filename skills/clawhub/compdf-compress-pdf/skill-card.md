## Description: <br>
ComPDF Compress PDF helps agents prepare ComPDF Server API requests to reduce PDF file size while balancing visual quality, resolution, and removal of non-essential document content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workflow teams use this skill to prepare ComPDF Server compression requests for PDFs, selecting supported compression flags, resolution settings, request mode, and result handling while preserving original files unless replacement is authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends documents to a third-party ComPDF service for compression. <br>
Mitigation: Confirm user authorization before upload, avoid confidential PDFs unless approved for ComPDF processing, and use asynchronous or presigned workflows for large or security-sensitive files. <br>
Risk: The skill uses a local ComPDF API key. <br>
Mitigation: Keep the API key in a private local file, pass it only as the x-api-key header, and never print, log, commit, or include it in generated examples. <br>
Risk: The bundled reference snapshot includes broader ComPDF API instructions beyond PDF compression. <br>
Mitigation: Use only the compression endpoint and optimization flags listed by the skill, and ignore unrelated API pages unless the skill is narrowed or split into separate capabilities. <br>


## Reference(s): <br>
- [ComPDF PDF Compression API](https://www.compdf.com/guides/api-reference/v2/compress-guides) <br>
- [ComPDF Compression Parameters](https://www.compdf.com/guides/api-reference/v2/optimization-flags) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>
- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/compdf-compress-pdf) <br>
- [ComPDF Publisher Profile](https://clawhub.ai/user/compdf-youna) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with endpoint details, request fields, and next steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API endpoint, method, content type, request fields, expected response fields, and polling or download steps; must not display API keys.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
