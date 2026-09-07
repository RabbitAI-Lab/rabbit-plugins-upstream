## Description:

Organizes QQ group homework for a selected date by collecting text and image attachments, generating A4 Word or PDF documents, checking page count, and optionally sending approved copies by email or WeChat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[laneovcc](https://clawhub.ai/user/laneovcc)

### License/Terms of Use:

MIT-0

## Use Case:

External users managing QQ class groups use this skill to gather homework from one or more QQ groups, preserve image attachments, create printable A4 homework documents, and send approved copies to email or WeChat recipients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill controls an already logged-in QQ browser outside the sandbox and caches session-derived homework data locally.

Mitigation: Use it only with the intended QQ account and trusted qqbrowser-skill executable path; periodically remove local JSON, image, DOCX, and PDF outputs that contain private class or child information.

Risk: Generated homework documents can be sent externally by email or WeChat.

Mitigation: Send documents only to explicitly approved recipients, and confirm recipient, subject, and attachment before using unattended or skip-confirmation flows.

Risk: PowerShell PDF conversion has unsafe path handling for crafted paths, especially paths containing single quotes.

Mitigation: Prefer trusted workspace paths and a safer PDF conversion route when available; avoid crafted file paths until the PowerShell conversion path handling is fixed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/laneovcc/skills/qq-group-homework-summarizer)
- [群作业接口参考](references/api.md)
- [故障排查与逆向记录](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with command examples; generated artifacts are JSON, DOCX, PDF, and image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an already logged-in QQ browser session; may write cached bkn values, homework JSON, downloaded images, DOCX/PDF documents, page-count output, and sent-marker files locally.]

## Skill Version(s):

1.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
