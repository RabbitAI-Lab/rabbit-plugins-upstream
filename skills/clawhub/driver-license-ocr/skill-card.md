## Description: <br>
Recognizes driver-license main and supplementary pages and extracts structured fields such as name, certificate number, permitted driving class, issue dates, archive number, and record information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scnet-sugon](https://clawhub.ai/user/scnet-sugon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and operations teams can call this skill from an agent to run OCR on a local driver-license image or PDF through SCNet and receive structured fields for authorized document-processing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver-license images, PDFs, and extracted OCR data contain sensitive personal information and are sent to SCNet's remote OCR service. <br>
Mitigation: Use the skill only for documents you are authorized to process, obtain appropriate consent, and delete local source files and OCR outputs when they are no longer needed. <br>
Risk: The SCNet API key could be exposed if pasted into chats, committed to source control, or stored with broad local permissions. <br>
Mitigation: Keep the key out of chats and repositories, prefer environment variables or a local config file, and restrict credential file permissions. <br>


## Reference(s): <br>
- [Sugon-Scnet OCR API Docs Summary](references/api-docs.md) <br>
- [Driver License OCR Fields Summary](assets/templates/fields-summary.md) <br>
- [SCNet Website](https://www.scnet.cn) <br>
- [ClawHub Skill Listing](https://clawhub.ai/scnet-sugon/skills/driver-license-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, JSON] <br>
**Output Format:** [JSON on stdout with human-readable error messages on failure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCNET_API_KEY; uploads the selected document to SCNet's remote OCR API; retries rate limits up to 3 times.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence, SKILL.md frontmatter, skill.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
