## Description: <br>
Generates professional PDF quotations, training proposals, and business documents from natural language, Markdown, or structured data, with Chinese and English content support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mebusw](https://clawhub.ai/user/mebusw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, consultants, and business users use this skill to collect quotation, training outline, proposal, customer, pricing, and branding details, then generate structured document data and a polished PDF quotation or proposal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may save customer details, pricing, quotation data, rendered HTML, and PDFs in a local output folder. <br>
Mitigation: Avoid entering sensitive customer or pricing information unless local storage is acceptable, and review or clean the output folder according to the user's data-handling requirements. <br>
Risk: The workflow depends on referenced rendering scripts and templates being present in the user's environment. <br>
Mitigation: Verify that the Python rendering script, Jinja2 template, logo asset, and Playwright PDF path exist before relying on generated documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mebusw/skills/jackyshen-gen-quotation) <br>
- [Server-resolved GitHub provenance](https://github.com/mebusw/jackyshen-gen-quotation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with structured JSON data and shell commands for generating local HTML and PDF files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local quotation data, rendered HTML, and Playwright-rendered PDF files in an output folder.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
