## Description:

QQBrowserUse is a browser automation CLI for AI agents that opens, navigates, interacts with websites, extracts page data, captures screenshots or downloads, and records or replays reusable browser tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qqbrowserteam](https://clawhub.ai/user/qqbrowserteam)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform isolated browser automation tasks, including page navigation, form interaction, data extraction, screenshots, downloads, and reusable playbook replay. It is intended for real browser tasks rather than static questions about web technologies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation can operate logged-in or sensitive websites and can save screenshots, downloads, or playbooks that contain private workflow details.

Mitigation: Install only when that access is acceptable, avoid sensitive sessions where possible, and remove saved artifacts or playbooks that contain private information.

Risk: Reusable playbook replay may repeat side-effecting actions such as posting, submitting, purchasing, deleting, or messaging.

Mitigation: Review side-effecting playbooks and variables before replay, prefer draft or sandbox flows, and require explicit authorization for live actions.

Risk: Sites may require CAPTCHA, MFA, QR login, or other human verification steps during automation.

Mitigation: Pause automation for the user to complete verification manually and resume only after the verification step is finished.

## Reference(s):

- [QQBrowserUse ClawHub Skill Page](https://clawhub.ai/qqbrowserteam/skills/qqbrowser-skill)
- [qqbrowser-skill PyPI Package](https://pypi.org/project/qqbrowser-skill/)
- [QQ Browser Homepage](https://browser.qq.com/)
- [QQBrowserUse Evaluation Report](https://bak.res.qq.com/nav/qqbrowser_skills/QQBrowserSkillReport.html)
- [Session Lifecycle](artifact/references/session-lifecycle.md)
- [Command Extended Reference](artifact/references/commands-extended.md)
- [Playbook Guide](artifact/references/playbook.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; browser command results may include text, Markdown, JSON strings, screenshots, or downloaded files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create reusable playbook JSON, screenshots, and downloaded files during browser automation workflows.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
