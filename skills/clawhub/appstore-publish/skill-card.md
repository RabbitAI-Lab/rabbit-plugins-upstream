## Description:

个人应用商店全流程 skill：发布构建好的安装包，登记上传并返回检查更新地址，同时指导把自动更新检查集成进应用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[justsosog](https://clawhub.ai/user/justsosog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill after building an application package to publish it to a personal app-store service and receive a download or update-check endpoint. They can also use it for guidance on integrating client-side automatic update checks across Android, Windows, macOS, and Linux applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create accounts, initiate paid activation, upload packages, and make releases public by default.

Mitigation: Require explicit user confirmation before registration, payment activation, uploads, or public release settings, and confirm the target app-store URL before execution.

Risk: The skill handles bearer upload tokens and includes client update examples where credentials could be exposed.

Mitigation: Store upload tokens outside client applications, prefer a backend proxy for private update checks, and avoid printing or committing tokens.

Risk: The skill documents destructive app and version deletion operations.

Mitigation: Require a separate confirmation step that names the app or version being deleted and verify the identifier against the app-store response before deletion.

Risk: The Android update sample downloads and installs packages from returned URLs.

Mitigation: Add package signature or checksum verification and use platform installation prompts before adopting the sample in production.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/justsosog/skills/appstore-publish)
- [Publisher profile](https://clawhub.ai/user/justsosog)
- [Default app-store service](https://appstore.qinghuan.fun)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, API examples, and platform-specific integration code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce upload commands, app-store API calls, update endpoint details, Android Kotlin snippets, and platform integration guidance.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
