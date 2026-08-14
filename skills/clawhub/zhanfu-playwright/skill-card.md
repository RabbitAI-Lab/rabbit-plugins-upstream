## Description:

Automates the ZhanFu WebDriver desktop client and store browsers through HTTP setup steps, then uses Playwright CDP for headed browser tasks after a WebDriver port is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhangzhang1997](https://clawhub.ai/user/zhangzhang1997)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to start or reuse the local ZhanFu client, open, close, create, list, and configure stores, update provided store account fields, and run headed Playwright automation inside a store browser after device-safety checks pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control the local ZhanFu client, open or close store browsers, create stores, update store account fields, set plugins, and clear caches.

Mitigation: Use it only when those local client and store-management actions are intended, and confirm destructive or credential-changing actions before execution.

Risk: The skill can use ZhanFu credentials and store account or password values when the user provides them.

Mitigation: Provide credentials only when login or account updates are intended, avoid sharing secrets in reusable prompts, and review requested account changes before submitting them.

Risk: The artifact stores local port, install-path, and store-ID state in JSON files.

Mitigation: Treat generated and cached state as local operational data and avoid publishing workspace copies that contain environment-specific paths or store identifiers.

Risk: Dependency ranges are broad enough that stricter environments may require tighter review.

Mitigation: Review and pin Playwright and requests versions before using the skill in a controlled production environment.

## Reference(s):

- [ZhanFu WebDriver API reference](artifact/reference.md)
- [ClawHub skill page](https://clawhub.ai/zhangzhang1997/skills/zhanfu-playwright)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP request examples, shell commands, and optional Python helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local ZhanFu desktop client and uses Playwright over CDP only after a WebDriver port is available.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
