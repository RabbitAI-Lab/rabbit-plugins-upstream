## Description:

Provides onboarding for SentiSense stock market skills, including API key setup and task routing across the SentiSense skill collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and market-research agents use this skill to set up SentiSense API access and choose the appropriate SentiSense stock-market skill for the user's request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated SentiSense calls require an API key and may expose preview or paid-dataset boundaries.

Mitigation: Store the key in SENTISENSE_API_KEY, use it only for read-only access, and disclose preview or partial data instead of treating it as complete.

Risk: Market research outputs could be mistaken for financial advice.

Mitigation: Present outputs as educational research and verify any trading decision independently.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Documentation](https://sentisense.ai/docs/api)
- [SentiSense API Key Signup](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)
- [ClawHub Publisher Profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and routing tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for downstream authenticated SentiSense calls; the onboarding skill is read-only.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
