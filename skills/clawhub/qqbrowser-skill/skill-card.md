## Description:

Browser automation CLI for AI agents that opens, navigates, interacts with websites, extracts data, captures screenshots, downloads content, analyzes open tabs, and records or replays browser playbooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qqbrowserteam](https://clawhub.ai/user/qqbrowserteam)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent users use this skill to automate browser workflows, inspect or extract web content, handle screenshots and downloads, and save reusable browser task playbooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation gives the agent power to navigate, click, submit forms, download files, and interact with authenticated pages.

Mitigation: Install only when that browser automation scope is acceptable, and review workflows before using the skill on sensitive or side-effecting sites.

Risk: Listing already-open tabs can reveal unrelated page titles and URLs to the agent.

Mitigation: Use open-tab analysis cautiously and keep unrelated sensitive tabs closed or out of scope before granting browser access.

Risk: Saved playbooks can persist replayable browser workflows, including actions that post, submit, purchase, delete, send messages, or publish content.

Mitigation: Review saved playbooks before replay, use test data or draft mode for side-effecting tasks, and avoid storing secrets or live credentials in variables.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qqbrowserteam/skills/qqbrowser-skill)
- [QQ Browser Homepage](https://browser.qq.com/)
- [PyPI Package](https://pypi.org/project/qqbrowser-skill/)
- [QQBrowserUse Evaluation Report](https://bak.res.qq.com/nav/qqbrowser_skills/QQBrowserSkillReport.html)
- [Command Extended Reference](references/commands-extended.md)
- [Session Lifecycle](references/session-lifecycle.md)
- [Playbook Guide](references/playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and browser automation command recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce file paths for downloaded files or saved playbooks when the browser workflow creates local artifacts.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
