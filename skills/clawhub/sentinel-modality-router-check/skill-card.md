## Description:

Confirms Sentinel's PII redaction guardrail survives routing through a modality-aware LiteLLM router to two different self-hosted model types, checks routing correctness per modality, and links the resulting Jaeger trace if tracing is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mark-stadtmueller](https://clawhub.ai/user/mark-stadtmueller)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to verify that a local Sentinel gateway continues to redact synthetic PII and route text and image requests to the expected backend model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill stops and restarts the local Sentinel gateway, briefly interrupting anything that depends on that gateway.

Mitigation: Install and run it only where the operator is authorized to restart the local Sentinel gateway and can tolerate the interruption.

Risk: If Telegram reporting is configured, failed probes can send up to 300 characters of backend response content to an external Telegram bot.

Mitigation: Leave TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID blank when third-party reporting is not acceptable, and remove or redact outbound snippets before adapting the probes to real user prompts.

Risk: Outdated dependency versions can introduce avoidable security exposure.

Mitigation: Use current patched dependency versions within the declared ranges.

## Reference(s):

- [Superwise PII redaction documentation](https://docs.superwise.ai/docs/pii-redaction)
- [Superwise MCP server](https://docs.superwise.ai/mcp)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [Console and Telegram text report with a structured JSON result from run()]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports pass/fail status for text and image probes, route matches, redaction/leak booleans, optional Telegram delivery status, and optional Jaeger trace details.]

## Skill Version(s):

1.0.1 (source: server release evidence and skill.py SKILL_META)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
