## Description:

Zhanfu Playwright automates Zhanfu client and store workflows through the WebDriver HTTP API, then uses Playwright over CDP after a store WebDriver port is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhangzhang1997](https://clawhub.ai/user/zhangzhang1997)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized operators use this skill to control Zhanfu stores, including opening or closing stores, listing or creating stores, changing store account data, configuring supported store settings, and running browser automation inside Zhanfu-managed store browsers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can request credentials and change or clear store account data.

Mitigation: Use it only with explicit authorization, confirm password or account changes before execution, and avoid retaining credentials beyond the active task.

Risk: The skill can close stores, exit or restart the Zhanfu client, configure plugins, and clear caches.

Mitigation: Confirm disruptive operations with the user first and stop on unsupported platform or client-version conditions.

Risk: Bundled local state files include cached port, path, and store-ID information.

Mitigation: Clear bundled cache and state files before first use and keep regenerated state local to the authorized environment.

## Reference(s):

- [Zhanfu WebDriver API Reference](artifact/reference.md)
- [ClawHub skill page](https://clawhub.ai/zhangzhang1997/skills/zhanfu-playwright)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON HTTP request examples, shell commands, and optional Python helper usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-authorized Zhanfu access and supported Zhanfu client versions before browser automation.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
