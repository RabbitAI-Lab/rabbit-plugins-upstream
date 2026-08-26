## Description:

qqbrowser-use lets AI agents automate QQ Browser sessions for navigation, page interaction, screenshots, downloads, structured extraction, and reusable playbook replay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qqbrowserteam](https://clawhub.ai/user/qqbrowserteam)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to control QQ Browser for web navigation, form interaction, screenshots, downloads, page-state inspection, structured data extraction, or replay of previously recorded browser workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation can affect real websites and accounts, including posting, submitting, purchasing, deleting, or messaging.

Mitigation: Require explicit user confirmation before replaying or manually executing workflows with real-account side effects.

Risk: Reusable playbooks may preserve sensitive workflow details or user-provided values if authors are careless.

Mitigation: Review saved playbooks before reuse and avoid storing passwords or sensitive personal data in them.

Risk: Sites may require CAPTCHA, MFA, QR login, device confirmation, or other human verification.

Mitigation: Pause automation for the user to complete verification manually and resume only after the verification step is complete.

## Reference(s):

- [QQ Browser homepage](https://browser.qq.com/)
- [qqbrowser-skill package](https://pypi.org/project/qqbrowser-skill/)
- [ClawHub skill page](https://clawhub.ai/qqbrowserteam/skills/qqbrowser-skill)
- [QQBrowserUse evaluation report](https://bak.res.qq.com/nav/qqbrowser_skills/QQBrowserSkillReport.html)
- [Command Extended Reference](references/commands-extended.md)
- [Playbook Guide](references/playbook.md)
- [Session Lifecycle](references/session-lifecycle.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON strings, file paths, browser screenshots, and shell command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persisted playbook JSON files for explicitly recorded reusable browser workflows.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
