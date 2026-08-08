## Description:

Automates Chinese domestic websites by connecting to a user's logged-in local Chrome session through CDP for authorized browsing, extraction, and JSON or CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[361066029](https://clawhub.ai/user/361066029)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to automate authorized account-visible workflows on Chinese domestic sites such as Xiaohongshu, Taobao, Bilibili, WeChat, Weibo, Zhihu, 12306, and SaaS backends. It is intended for cases where a normal browser session is already logged in and the agent needs to preserve that login state while extracting or operating on data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose data available to a logged-in Chrome profile.

Mitigation: Use a dedicated Chrome profile with only the accounts and sites needed for the task.

Risk: Automation may run against sensitive pages such as financial, identity, order, private-message, or business-admin areas.

Mitigation: Review each target URL before execution and avoid sensitive areas unless the user explicitly confirms the need.

Risk: Custom extraction JavaScript can access page-visible data in the active browser context.

Mitigation: Run only reviewed extraction scripts and do not execute arbitrary JavaScript from untrusted sources.

Risk: Site selectors and anti-abuse controls can change, causing inaccurate extraction or blocked sessions.

Mitigation: Verify selectors on the live page, keep request rates low, and require manual completion for CAPTCHA or slider challenges.

## Reference(s):

- [Chrome setup and troubleshooting](artifact/references/setup.md)
- [Chinese site selector and anti-abuse notes](artifact/references/sites.md)
- [ClawHub skill page](https://clawhub.ai/361066029/skills/cn-browser-automation)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files]

**Output Format:** [Markdown guidance with Python and shell command examples; scripts can write JSON and optional CSV files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Playwright with a local Chrome CDP endpoint and may operate within an existing logged-in browser profile.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
