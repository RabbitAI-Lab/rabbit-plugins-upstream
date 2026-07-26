## Description: <br>
Writes technical articles and publishes them to CSDN using browser automation, QR-code login, optional Telegram QR delivery, and a Chinese blog-writing workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[c4chuan](https://clawhub.ai/user/c4chuan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and content creators use this skill to draft Chinese technical posts, check news items against recent Notion records, and publish approved Markdown articles to CSDN through browser automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses browser automation, local session persistence, CSDN credentials, Notion credentials, Telegram notifications, and local draft storage. <br>
Mitigation: Install only for intended CSDN publishing workflows, use least-privilege CSDN and Notion credentials, keep credential and draft paths private, and review stored cookies and drafts before reuse. <br>
Risk: QR-code login images can be sent through Telegram when notification support is enabled. <br>
Mitigation: Use only a trusted bot and chat path for QR delivery, or disable Telegram notification behavior when that channel is not trusted. <br>
Risk: Notion duplicate checks and content reuse can change what gets published or skipped. <br>
Mitigation: Configure Notion duplicate checks deliberately, review the returned duplicate status before publishing, or disable the Notion flow when it is not needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/c4chuan/skills/csdn-publisher) <br>
- [CSDN Markdown Editor](https://editor.csdn.net/md) <br>
- [CSDN Login](https://passport.csdn.net/login) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prose with inline shell commands, browser actions, script invocations, and local file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local Markdown drafts, CSDN cookie files, QR-code screenshots, and Notion duplicate-check results during operation.] <br>

## Skill Version(s): <br>
2.3.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
