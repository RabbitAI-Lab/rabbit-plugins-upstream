## Description: <br>
Converts PDF files into Markdown with ComPDF for knowledge-base ingestion, developer documentation, content repurposing, research workflows, and PDF-to-Markdown requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content teams, and AI agents use this skill to plan ComPDF Server API requests that convert PDFs into structured Markdown for knowledge ingestion, documentation, publishing, and research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs and a local ComPDF API key are used with an external ComPDF service. <br>
Mitigation: Use only when organizational policy permits ComPDF processing and retention behavior; keep the API key in a private local file and never display it. <br>
Risk: Incorrect endpoint or request-field guidance could lead to failed conversions or unintended document processing. <br>
Mitigation: Use only the supported PDF to Markdown operation and rely on the bundled official API reference snapshot for endpoint paths, fields, request modes, and response fields. <br>


## Reference(s): <br>
- [ComPDF PDF To Markdown release page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-markdown) <br>
- [ComPDF endpoint index](artifact/references/endpoint-index.md) <br>
- [Official ComPDF V2 API reference snapshot](artifact/references/official-api-reference.md) <br>
- [ComPDF PDF to Markdown API reference](https://www.compdf.com/guides/api-reference/v2/pdf-to-md) <br>
- [ComPDF authentication documentation](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF request workflow documentation](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown text with endpoint details, request fields, expected response fields, and optional shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the next polling or download step; must not include API keys in output.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
