## Description: <br>
ComPDF Page Editor helps agents prepare ComPDF Server API request plans to merge, split, rotate, insert, delete, and extract PDF pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document automation teams use this skill to assemble, clean up, and restructure PDF documents before review, filing, delivery, or downstream automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDF files are sent to ComPDF's external service for processing. <br>
Mitigation: Use the skill only for documents that are appropriate to process with ComPDF's external service, and prefer asynchronous or presigned workflows for large, batch, or security-sensitive uploads as documented by the skill. <br>
Risk: The skill reads a local ComPDF API key file. <br>
Mitigation: Store the key only in the documented private key file, pass it only as the x-api-key header, and do not include the key in code, logs, examples, or output. <br>
Risk: The bundled API reference includes broader ComPDF capabilities outside this skill's scope. <br>
Mitigation: Use only the six page-management operations named by the skill: merge, split, rotate, insert, delete, and extract. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/compdf-youna/skills/compdf-page-editor) <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF API sign-in](https://www.compdf.com/compdf-portal/signin?utm_source=clawhub&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=clawhub_compdfkit_skills_en) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with endpoint, request fields, response fields, and next-step instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill produces request plans and handling guidance; it does not include or display API keys.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
