## Description: <br>
Cn Pdf Editor helps an agent provide local PDF editing workflows for text edits, image insertion, watermarking, annotations, merging, splitting, page reordering, and signatures using the bundled PyMuPDF-based tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[freedompixels](https://clawhub.ai/user/freedompixels) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, document operators, and agents use this skill to edit PDFs locally, including document tweaks, watermarking, annotations, page management, merging, splitting, and signatures. It is best suited for local document processing where users review resulting PDFs before relying on them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local PDF editor web server is exposed to the network without authentication. <br>
Mitigation: Bind the service to 127.0.0.1 before use, run it only on trusted networks, close it when finished, and avoid highly sensitive PDFs until the exposure is fixed. <br>
Risk: PDF edits may alter document meaning or leave unexpected formatting artifacts. <br>
Mitigation: Review the edited PDF before sharing or relying on it for contracts, quotes, or other business documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/freedompixels/skills/cn-pdf-editor) <br>
- [Publisher profile](https://clawhub.ai/user/freedompixels) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and code-oriented usage details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide local file edits through the bundled PDF editor; users should review generated PDFs and avoid exposing the unauthenticated web service on untrusted networks.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
