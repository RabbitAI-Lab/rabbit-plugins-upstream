## Description:

Converts user-selected PDF files or images into editable Word documents through SCNet's asynchronous document conversion service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and document operations teams use this skill to submit PDF conversion jobs, poll for completion, and receive a temporary download link for the generated Word document.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected PDF or image is uploaded to SCNet for remote processing, so file contents leave the local environment.

Mitigation: Warn the user before execution, require confirmation, and avoid confidential, regulated, or business-sensitive documents unless SCNet data handling and retention terms have been reviewed.

Risk: The conversion result is returned as a temporary download link.

Mitigation: Download results promptly and avoid sharing the returned link beyond the intended user or workflow.

## Reference(s):

- [SCNet PDF to Word API docs](references/api-docs.md)
- [SCNet website](https://www.scnet.cn)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/pdf-to-word)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON or plain-text status messages containing task status, errors, or a temporary .docx download URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an SCNET_API_KEY and sends the selected input file to SCNet for remote processing.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact frontmatter and changelog list 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
