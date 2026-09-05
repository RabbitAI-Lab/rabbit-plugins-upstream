## Description:

LLM Gateway Hub helps agents and developers configure and operate a local command-line gateway for multiple OpenAI-compatible model providers with budget checks, usage ledgering, and API key handling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent operators use this skill to centralize calls to configured LLM providers, manage local provider credentials, enforce monthly budget limits, and inspect model usage costs. It is suited to personal or team workflows that need one gateway across hosted and local model backends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider API keys are stored in a local JSON configuration file and may be exposed if that file is synced, backed up, or shared without secret protection.

Mitigation: Keep gateway_config.json private to the local machine, restrict file permissions, avoid committing or sharing it, and rotate keys if exposure is suspected.

Risk: Prompts and image requests are sent to whichever model provider endpoints the user configures, so sensitive data may leave the machine during normal gateway calls.

Mitigation: Use only trusted base_url values, review provider data handling terms, and avoid sending sensitive prompts unless the configured provider is approved for that data.

Risk: Budget and pricing controls depend on accurate local provider configuration and may be misleading if prices or model IDs are stale.

Mitigation: Start with low budgets, verify current provider pricing and model identifiers before use, and review the generated usage ledger regularly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/llm-gateway-hub)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://nomos.ai)
- [Gateway configuration template](references/gateway_config.template.json)
- [New provider integration guide](references/接入新平台指引.md)
- [Security audit report](安全审计报告.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local configuration steps, provider setup guidance, command examples, budget and ledger inspection guidance, and code-oriented integration notes.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter remains 1.0.3 with no file modifications in this version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
