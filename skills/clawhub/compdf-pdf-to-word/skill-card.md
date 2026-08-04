## Description: <br>
Convert PDF files into editable Word documents with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and document operations teams use this skill to prepare ComPDF PDF-to-Word API requests for contracts, reports, forms, proposals, localization, and business revision workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a local ComPDF API key and sends selected documents to an external ComPDF service. <br>
Mitigation: Install only when that data flow is acceptable, keep the API key in a private local key file, and send documents only after the affected files and operation are confirmed. <br>
Risk: The bundled reference files describe many document operations beyond PDF-to-Word. <br>
Mitigation: Use only the PDF-to-Word operation supported by the skill and verify the selected endpoint, request fields, and response fields against the matching reference section. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF API sign-in](https://www.compdf.com/compdf-portal/signin?utm_source=clawhub&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=clawhub_compdfkit_skills_en) <br>
- [ClawHub skill page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-word) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with endpoint details, request fields, expected response fields, and follow-up polling or download steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces request plans and command-oriented guidance; it should not expose API keys in examples, logs, code, or output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
