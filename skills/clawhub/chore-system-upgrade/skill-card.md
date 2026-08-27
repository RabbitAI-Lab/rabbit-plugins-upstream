## Description:

A Xiaohongshu browser toolkit for AI agents and command-line users that supports search, content reading, login, publishing, comments, likes, collections, templates, strategy state, and SOP workflows through a Python Playwright CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deliciousbuding](https://clawhub.ai/user/deliciousbuding)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and AI agent users use this skill to automate Xiaohongshu discovery, account-session checks, content preparation, publishing, and account interactions while preserving explicit confirmation for account-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a real Xiaohongshu account through publishing, commenting, replying, liking, collecting, and logout actions.

Mitigation: Use a dedicated test account where possible and require explicit user review of the target account, content, media, visibility, and action type before any account-changing command runs.

Risk: Persistent browser sessions, cookies, QR images, profile metadata, and security parameters may expose account access if copied, logged, or uploaded.

Mitigation: Protect or clear local Xiaohongshu profile state when finished, and never include cookies, QR codes, full xsec_token values, account identifiers, or profile files in logs, issues, or shared artifacts.

Risk: Captcha, login, or security-verification pages can appear during automation.

Mitigation: Stop automated actions on these pages, switch to headed mode, and let the user complete the verification manually rather than retrying or attempting bypass.

Risk: The security review flags anti-detection behavior, login-popup bypass behavior, and real-account action paths as suspicious.

Mitigation: Install only after reviewing platform rules and account-enforcement risk; keep navigation intervals and cooldowns enabled and avoid high-frequency bulk scraping or bulk interaction.

Risk: A publish result of submitted_unconfirmed may mean the site accepted the submission even though success was not verified.

Mitigation: Review the creator page manually and do not automatically retry, because retrying can create duplicate posts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/deliciousbuding/skills/chore-system-upgrade)
- [CLI command reference](docs/API.md)
- [Installation guide](docs/INSTALL.md)
- [Security guide](docs/SECURITY.md)
- [Reference implementations](docs/REFERENCE.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [JSON CLI responses, Markdown or plain-text guidance, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnostics are written to stderr; account-changing actions require explicit user confirmation before execution.]

## Skill Version(s):

1.5.0 (source: pyproject.toml, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
