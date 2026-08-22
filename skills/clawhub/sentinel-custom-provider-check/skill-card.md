## Description:

Verifies that Sentinel's PII and secret redaction guardrail survives routing through CUSTOM_PROVIDERS to a self-hosted OpenAI-compatible backend by running a synthetic probe and checking whether the result is redacted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mark-stadtmueller](https://clawhub.ai/user/mark-stadtmueller)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to confirm that Sentinel redaction still applies when traffic is routed to a self-hosted OpenAI-compatible model through CUSTOM_PROVIDERS. It helps distinguish a true custom-provider guardrail pass from redaction that may have happened elsewhere in the calling path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stops and restarts the local Sentinel gateway during the check.

Mitigation: Run it only when a gateway restart is acceptable and avoid using it during active gateway traffic.

Risk: Check results can optionally be sent to Telegram.

Mitigation: Leave TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID unset when local-only stdout reporting is preferred.

Risk: Failure details may include raw backend output from the synthetic probe.

Mitigation: Use only synthetic probe values and review sharing destinations before enabling Telegram delivery.

## Reference(s):

- [Sentinel Getting Started](https://docs.superwise.ai/docs/getting-started)
- [Sentinel MCP Server](https://docs.superwise.ai/mcp)
- [ClawHub Skill Page](https://clawhub.ai/mark-stadtmueller/skills/sentinel-custom-provider-check)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Python dictionary and stdout text, with optional Telegram message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports pass/fail status, whether Telegram delivery was sent, and probe details.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill.py SKILL_META)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
