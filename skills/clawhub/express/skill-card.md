## Description:

查快递物流轨迹与签收状态，支持自动识别公司与顺丰等校验。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents use this skill to query express shipment status, recent tracking events, delivery state, and supported carrier codes through JisuAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tracking numbers, carrier codes, the JisuAPI key, and sometimes the last four digits of a phone number are sent to JisuAPI.

Mitigation: Use a limited API key where possible, avoid querying highly sensitive shipments, and rotate the key if URL logs may have exposed it.

Risk: Command-line use can be unsafe if raw user input is interpolated into a shell command.

Mitigation: Pass user-provided fields as structured JSON arguments and apply strict quoting when a shell invocation is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jisuapi/skills/express)
- [JisuAPI](https://www.jisuapi.com/)
- [JisuAPI express documentation](https://www.jisuapi.com/api/express)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON responses and concise natural-language shipment summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JISU_API_KEY; some carriers require the last four digits of a phone number.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
