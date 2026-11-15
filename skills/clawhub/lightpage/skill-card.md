## Description:

Publishes and manages HTML, Markdown, TXT, and static websites on Lightpage, and supports reading works, analytics, sharing QR codes, account actions, and messaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuchaokn](https://clawhub.ai/user/zhuchaokn)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and site owners use this skill to publish and manage static HTML or documents on Lightpage, share links, read published works, and handle requested analytics and platform interactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security evidence reports a benign verdict with medium confidence and partial scanning, and notes social actions and standalone image hosting alongside Lightpage publishing.

Mitigation: Review the skill's scope and authorize each requested publishing or communication action explicitly.

Risk: Published files can be reached through a share link, including works marked private; uploaded secrets could therefore be exposed.

Mitigation: Review the selected files and visibility before publishing, and keep credentials and private data out of uploads.

Risk: Local credentials enable account and work management actions.

Mitigation: Protect the local credential files and do not include tokens in published content or shared output.

## Reference(s):

- [Lightpage homepage](https://lightpage.hqdx.store/)
- [Lightpage works management](https://lightpage.hqdx.store/manage/)
- [Publishing guide](references/publishing.md)
- [Works management and analytics](references/management.md)
- [Preflight review guide](references/preflight.md)
- [Account and authorization guide](references/account.md)
- [Mail guide](references/mail.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance, Files]

**Output Format:** [Markdown with links and shell commands; may include a QR code image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include published work links, status and analytics summaries, and locally generated QR code images.]

## Skill Version(s):

0.9.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
