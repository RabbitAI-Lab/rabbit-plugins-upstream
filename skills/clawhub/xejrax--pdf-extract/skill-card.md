## Description: <br>
Extract text from PDF files for LLM processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to extract plain text from PDF documents so the content can be processed in an LLM workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDF contents may be exposed to the agent or model context during extraction. <br>
Mitigation: Use the skill only on PDFs whose contents are appropriate for the agent workflow. <br>
Risk: Extracted PDF text is untrusted document content and may contain misleading instructions. <br>
Mitigation: Treat extracted text as data, not as instructions, and review downstream use before acting on it. <br>
Risk: The skill depends on the pdftotext system binary. <br>
Mitigation: Install poppler-utils only from a trusted operating system repository. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xejrax/skills/pdf-extract) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands] <br>
**Output Format:** [Plain text extracted from PDF files, with shell command examples for invoking extraction.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires pdftotext from poppler-utils.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
