## Description:

Clawdbot documentation expert with decision tree navigation, search scripts, doc fetching, version tracking, and config snippets for all Clawdbot features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support agents use this skill to answer Clawdbot setup, troubleshooting, configuration, automation, installation, and documentation-navigation questions. It can provide Markdown guidance, cite Clawdbot documentation paths, and suggest configuration snippets or bundled helper commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configuration snippets can involve provider tokens or session paths that may expose credentials or private session data if copied without secure handling.

Mitigation: Store provider tokens in environment variables or a secrets manager, avoid committing secrets, and keep session directories private.

Risk: Gateway examples may bind services to 0.0.0.0, which can unintentionally expose a local service to a network.

Mitigation: Bind the gateway to localhost by default; use remote access only with authentication, TLS, and firewall controls.

Risk: The bundled search, fetch, index, and change-tracking scripts are mostly placeholders and may not provide a complete live documentation search system.

Mitigation: Treat script output as lightweight guidance and verify answers against the referenced Clawdbot documentation before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/clawddocs)
- [Clawdbot Discord provider documentation](https://docs.clawd.bot/providers/discord)
- [Common Clawdbot configuration snippets](snippets/common-configs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference bundled helper scripts; full-text index guidance depends on qmd and the scripts are lightweight placeholders in this release.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
