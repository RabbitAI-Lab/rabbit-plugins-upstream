## Description:

zhanfu-playwright helps agents control the local ZhanFu WebDriver client and shop browsers by using ZhanFu HTTP APIs first, then Playwright over CDP after a WebDriver port is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhangzhang1997](https://clawhub.ai/user/zhangzhang1997)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a local ZhanFu desktop client, manage shop browsers, and perform guided browser automation through Playwright after the ZhanFu WebDriver connection is established.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control the user's local ZhanFu client and shop browsers, including destructive or account-changing actions such as clearing cache, changing credentials, creating shops, closing shops, or exiting ZhanFu.

Mitigation: Confirm the exact shop and requested action before executing destructive or account-changing operations.

Risk: The skill may handle ZhanFu account credentials during login.

Mitigation: Ask for credentials only when the user is deliberately logging into the local ZhanFu instance, and do not reuse or infer credentials.

Risk: Some cache, plugin, download-directory, and low-kernel browser automation paths are unsupported or risky on macOS.

Mitigation: Stop before unsupported macOS actions and require a supported browser kernel before proceeding with Playwright automation.

## Reference(s):

- [ZhanFu WebDriver API reference](artifact/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented status output from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local ZhanFu client, Playwright, requests, and user-provided credentials only when deliberately logging in.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
