## Description:

QQ群作业整理 helps an agent fetch QQ group homework for a requested date, including image attachments, generate formatted A4 Word/PDF homework documents, and optionally send them by email or WeCom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[laneovcc](https://clawhub.ai/user/laneovcc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to collect homework assigned through QQ group homework, preserve text and image attachments, create printable Word or PDF files, and send the resulting document to an approved recipient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a logged-in QQ browser session and can store local homework data, image attachments, generated documents, and bkn values.

Mitigation: Use it only for QQ groups the operator is authorized to access, review generated files, and remove local JSON, image, DOCX, and PDF artifacts after use.

Risk: The skill can send generated homework files through email or WeCom channels.

Mitigation: Confirm the recipient, channel, subject, and attachment before sending unless the user has explicitly pre-authorized unattended delivery.

Risk: Browser automation outside the sandbox and PowerShell/Word COM PDF conversion increase local execution risk.

Mitigation: Run in a trusted local environment, keep dependencies current, and treat sandbox-disabled browser and Word COM paths as elevated local-risk operations.

Risk: Unattended scheduling could repeatedly send or print documents if the workflow is not bounded.

Mitigation: Use a narrow schedule window, require a reviewed destination and prompt, and write idempotency markers only after successful delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/laneovcc/skills/qq-group-homework-summarizer)
- [群作业接口参考](references/api.md)
- [故障排查与逆向记录](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated local JSON, image, DOCX, and PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local QQ homework cache/configuration files, downloaded images, Word documents, PDFs, and send approved attachments through configured mail or WeCom channels.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
