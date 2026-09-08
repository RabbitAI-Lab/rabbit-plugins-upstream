## Description:

用原生 Chrome DevTools Protocol 驱动千问浏览器（qianwen.exe），复用真实登录态做办公自动化。当用户要让"千问浏览器"自动打开网页、填表、点击、抓取内容、截图，或提到 xbrowser/agent-browser 驱动千问失败时，使用本技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to automate a real logged-in Qianwen browser session for browsing, form entry, clicking, content extraction, screenshots, and page-level JavaScript execution through native CDP commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automate a real logged-in Qianwen browser through a persistent local CDP port, so unintended clicks, form submissions, screenshots, or JavaScript execution can affect the user's account or page state.

Mitigation: Use it only on intended pages, confirm high-impact external actions before execution, and avoid accounts or pages where unintended browser actions would be high impact.

Risk: The shortcut patching helper can modify Windows shortcut arguments to enable the CDP port.

Mitigation: Run the patching helper in dry-run mode first, review affected shortcuts, and keep the unapply path available before making changes.

Risk: Launching or relaunching Qianwen can close the user's current browser process or disrupt the active profile.

Mitigation: Prefer checking for and connecting to an existing CDP-enabled instance, launch only when explicitly needed, and keep a rollback path for changed browser state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/qianwen-cdp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce browser screenshots as PNG files when the screenshot command is used.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
