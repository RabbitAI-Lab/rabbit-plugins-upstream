## Description:

Overwing helps agents check text for safety, personal data, self-harm, sexual content, and severity before they send, act on, or show that text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frod27](https://clawhub.ai/user/frod27)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to moderate model output, screen incoming messages, detect personal data, and decide whether text should pass, be reviewed, or be rewritten before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evaluated text is sent to Overwing's external service.

Mitigation: Do not submit secrets or highly sensitive content unless external processing is acceptable.

Risk: Signup and API usage can involve credentials or API keys.

Mitigation: Use a dedicated API key, avoid reused passwords for signup, and do not print API keys back into chat.

Risk: Optional x402 payments or SDK/MCP packages can spend funds or add package supply-chain exposure.

Mitigation: Use wallet spending only with human permission and pin or review optional MCP and SDK packages before running them.

## Reference(s):

- [Overwing homepage](https://overwing.ai)
- [Overwing agent guide](https://overwing.ai/llms.txt)
- [Overwing API reference](https://overwing.ai/docs)
- [Overwing content-safety rule set](https://overwing.ai/api/v1/rule-sets/content-safety)
- [Overwing x402 evaluate endpoint](https://overwing.ai/api/x402/evaluate)
- [ClawHub skill page](https://clawhub.ai/frod27/skills/overwing)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and an OVERWING_API_KEY for account-based API calls; x402 pay-per-request use requires a funded wallet and human permission.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
