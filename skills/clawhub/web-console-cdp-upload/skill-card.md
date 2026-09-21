## Description:

平台只有网页后台、没有上传 API 时，用本机已装的 Chrome/Edge + CDP 自动化走完上传、发布和填表流程，复用登录态并支持给文件选择框设置文件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill when a web console is the only available path for uploads, publishing, or form submission. It guides an agent through controlling a user-launched Chrome or Edge session with CDP, evaluating page state, filling controlled inputs, selecting files, submitting, and verifying the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent to control a logged-in browser session, which can expose account state or perform unintended account-changing actions.

Mitigation: Use a temporary browser profile when possible, avoid daily profiles for protected sites, and require explicit confirmation before submit, publish, or account-changing actions.

Risk: The skill includes advice about bypassing site protections such as anti-bot or WAF controls.

Mitigation: Use that guidance only with clear authorization and an approved automation path from the site owner.

Risk: A browser started with a remote debugging port can remain available after the task is complete.

Mitigation: Close the debugging browser after use and verify the CDP endpoint is no longer reachable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oracis/skills/web-console-cdp-upload)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is intended for an agent operating a local browser debugging session and should be reviewed before actions that submit, publish, or change account state.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
