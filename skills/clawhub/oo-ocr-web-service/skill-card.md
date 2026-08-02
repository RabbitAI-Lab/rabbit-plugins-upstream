## Description: <br>
OCR Web Service lets agents use OOMOL's oo CLI to retrieve account information and process public image or PDF URLs through OCR Web Service for extracted text or output file metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to check OCR Web Service account status and submit public image or PDF URLs for OCR through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documents submitted for OCR may contain sensitive content and are sent through OOMOL and OCR Web Service. <br>
Mitigation: Only process documents whose contents the user is authorized to share with those services. <br>
Risk: First-time setup may require installing the OOMOL oo CLI from a remote installer. <br>
Mitigation: Review the installer and install guide before running them, and skip installation when the CLI is already available. <br>
Risk: OCR actions can fail when authentication, connector scope, or billing status is missing or expired. <br>
Mitigation: Use the setup flow only after the matching error occurs, resolve that specific account issue, and then retry. <br>


## Reference(s): <br>
- [OCR Web Service homepage](https://www.ocrwebservice.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return account limits, remaining pages, subscription metadata, extracted OCR text, or output file metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
