## Description:

Introduces SentiSense stock-market skills, explains API-key setup, and directs agents to the skill best suited to a user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this onboarding skill to configure a SentiSense API key and choose the appropriate read-only stock-market data skill for a request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using this skill requires a SentiSense API key and network access to SentiSense.

Mitigation: Provide the key through a protected credential or environment variable; avoid displaying it, and allow only the necessary SentiSense HTTPS requests.

Risk: Market-data responses may be incomplete or mistaken for financial advice.

Mitigation: Identify preview or missing data, present findings as research and educational information, and do not execute trades.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API documentation](https://sentisense.ai/docs/api)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests to a task-specific SentiSense skill; does not execute trades.]

## Skill Version(s):

1.4.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
