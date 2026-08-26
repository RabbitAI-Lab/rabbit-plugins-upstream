## Description:

Xiaohongshu Skill is a Python Playwright agent toolkit for searching and reading Xiaohongshu content, managing browser login sessions, preparing or publishing posts, and performing account interactions with JSON output and required confirmation for write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deliciousbuding](https://clawhub.ai/user/deliciousbuding)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, agent operators, and social media teams use this skill to run structured Xiaohongshu discovery, reading, publishing preparation, and account interaction workflows through a JSON CLI. It is intended for accounts the user controls, with explicit confirmation before actions that change account state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill keeps a persistent Xiaohongshu browser session and can act through a real account.

Mitigation: Use a dedicated or test account, protect local session state such as ~/.xiaohongshu like credentials, and avoid sharing account data, QR codes, cookies, screenshots, or full security tokens.

Risk: Write commands can publish, comment, reply, like, collect, unlike, uncollect, or log out.

Mitigation: Require human review and explicit confirmation before each account-changing command, execute only the confirmed single action, and manually review submitted_unconfirmed publish results without automatic retry.

Risk: The security evidence reports stealth browser behavior, login-popup suppression, and platform-evasion behavior that may violate Xiaohongshu rules.

Mitigation: Review platform rules before use, keep built-in cooldowns enabled, avoid high-frequency bulk scraping or bulk interaction, and stop automation on captcha, login, or security-verification pages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deliciousbuding/skills/xiaohongshu-skill)
- [Publisher profile](https://clawhub.ai/user/deliciousbuding)
- [README](artifact/README_EN.md)
- [CLI API](artifact/docs/API.md)
- [Installation guide](artifact/docs/INSTALL.md)
- [Security guide](artifact/docs/SECURITY.md)
- [Reference implementations and attribution](artifact/docs/REFERENCE.md)
- [Third-party notices](artifact/THIRD_PARTY_NOTICES.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON CLI output with stderr diagnostics; Markdown documentation for setup and operating guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent integrations should parse the status field, treat submitted_unconfirmed as requiring manual review, and obtain explicit user confirmation before write commands.]

## Skill Version(s):

1.5.1 (source: ClawHub release evidence created 2026-08-23, pyproject.toml, CHANGELOG dated 2026-08-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
