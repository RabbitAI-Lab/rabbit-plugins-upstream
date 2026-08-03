## Description: <br>
Add or remove text and image watermarks in PDFs with ComPDF for branding, draft review marks, document control, cleanup, and final-delivery preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and document operations teams use this skill to prepare ComPDF Server API requests for adding or removing text and image watermarks in PDFs. It is intended for authorized watermarking, cleanup, document control, and final-delivery preparation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs are sent to the external ComPDF service for processing. <br>
Mitigation: Use the skill only for authorized documents and avoid confidential, regulated, or third-party files unless the user has approved that external processing. <br>
Risk: A ComPDF API key is stored locally for repeated use. <br>
Mitigation: Keep the key in the documented private key file, do not commit or display it, and pass it only through the x-api-key request header. <br>
Risk: The bundled API snapshot includes broader ComPDF endpoints than this watermark-focused skill needs. <br>
Mitigation: Restrict use to the supported add-watermark and remove-watermark endpoints listed by the skill, and verify endpoint paths and fields against the matching reference headings. <br>
Risk: Watermark removal or replacement can affect document control and attribution. <br>
Mitigation: Confirm authorization before removing or replacing an existing watermark and preserve original files unless replacement is explicitly requested. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF Add Watermark API Guide](https://www.compdf.com/guides/api-reference/v2/watermark-guides) <br>
- [ComPDF Remove Watermark API Guide](https://www.compdf.com/guides/api-reference/v2/del-watermark-guides) <br>
- [ComPDF Authentication Guide](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow Guide](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance, shell commands] <br>
**Output Format:** [Markdown with endpoint details, request fields, expected response fields, and next-step guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API key file setup guidance and request or polling commands; API keys should not be displayed in output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
