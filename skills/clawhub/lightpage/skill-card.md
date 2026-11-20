## Description:

Publishes HTML, Markdown, TXT, and static sites to Lightpage, and helps read and manage published works and use related platform features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuchaokn](https://clawhub.ai/user/zhuchaokn)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers use Lightpage to publish and share static works, read or manage existing works, and access features such as account linking, access controls, comments, and messaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing a single HTML file may also include a sibling Agent.md file.

Mitigation: Review that file's contents and publish it only when it is intended for sharing.

Risk: The scan reports capabilities beyond the stated Lightpage publishing purpose, and its coverage is incomplete.

Mitigation: Review the relevant capability guide and authorize only the specific account, messaging, access, or publishing action requested.

## Reference(s):

- [Lightpage homepage](https://lightpage.hqdx.store/)
- [Lightpage management page](https://lightpage.hqdx.store/manage/)
- [ClawHub skill listing](https://clawhub.ai/zhuchaokn/skills/lightpage)
- [Publishing and static content](references/publishing.md)
- [Preflight review](references/preflight.md)
- [Work and account management](references/management.md)
- [Account and authorization](references/account.md)
- [Platform capabilities](references/capabilities.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Links]

**Output Format:** [Text and Markdown, including published work URLs and service results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Published HTML, Markdown, TXT, or static site content is hosted as static files.]

## Skill Version(s):

0.16.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
