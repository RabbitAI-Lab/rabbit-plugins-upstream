## Description:

Read first when using any SentiSense stock market skill: API key setup and which skill owns each task. Patterns to adapt, not scripts. The user's task always wins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this onboarding skill to configure a SentiSense API key and choose the most specific SentiSense stock-market skill for a user task. It frames outputs as research and educational content, not financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key in the agent runtime environment.

Mitigation: Install only in environments where sharing SENTISENSE_API_KEY is acceptable, and use a key scoped for read-only data access.

Risk: Stock-market outputs may be mistaken for financial advice.

Mitigation: Present outputs as research and educational content, state when data is preview or partial, and avoid trade recommendations.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key Setup](https://app.sentisense.ai/get-api-key)
- [SentiSense Full API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Documentation](https://sentisense.ai/docs/api)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)
- [ClawHub Publisher Profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for SentiSense API use; guidance is read-only and educational.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
