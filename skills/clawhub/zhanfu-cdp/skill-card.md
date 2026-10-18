## Description:

Helps agents manage ZhanFu stores through the local app and automate store browser pages with Playwright after obtaining a WebDriver port.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhangzhang1997](https://clawhub.ai/user/zhangzhang1997)

### License/Terms of Use:

MIT-0

## Use Case:

ZhanFu store operators and developers use this skill to open and manage stores through their logged-in local app, and to automate browser pages when requested. It requires a supported ZhanFu installation and Node.js.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Store creation, credential changes, and plugin settings can alter a logged-in account's stores.

Mitigation: Allow these operations only when explicitly authorized by the account holder; review the target store and requested change first.

Risk: Cache clearing is irreversible and the helper does not enforce confirmation.

Mitigation: Require explicit confirmation outside the helper before clearing a store's or all stores' cache.

## Reference(s):

- [ZhanFu CDP on ClawHub](https://clawhub.ai/zhangzhang1997/skills/zhanfu-cdp)
- [ZhanFu API reference](artifact/reference.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown with commands and operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report store identifiers, operation status, and WebDriver ports.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
