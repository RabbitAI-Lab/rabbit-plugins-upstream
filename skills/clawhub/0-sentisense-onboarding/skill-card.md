## Description:

Read first when using any SentiSense stock market skill: API key setup and which skill owns each task. Patterns to adapt, not scripts. The user's task always wins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this onboarding skill to configure the SentiSense API key and choose the appropriate SentiSense market-data skill before making read-only market research requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key, which could be exposed if printed or copied into prompts.

Mitigation: Store the key in an environment variable or host credential store, reference the secret by name, and verify access with a low-cost call rather than printing the value.

Risk: Optional npx CLI examples execute third-party package code.

Mitigation: Prefer the documented API or a trusted host credential flow when possible; use the pinned CLI example only when that execution path is acceptable.

Risk: Market data outputs can be mistaken for financial advice or complete paid-dataset records.

Mitigation: Present outputs as educational research, never trading advice, and clearly state when a response is a preview or when data is absent.

Risk: Rapid parallel requests can hit SentiSense rate limits.

Mitigation: Page serially and honor Retry-After responses before retrying.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Key Setup](https://app.sentisense.ai/get-api-key)
- [SentiSense Skill API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Documentation](https://sentisense.ai/docs/api)
- [Grok Bot Setup Guide](https://sentisense.ai/blog/how-to-add-market-data-to-your-grok-bot/)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, markdown]

**Output Format:** [Markdown guidance with inline shell commands and routing tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for SentiSense service calls; the onboarding content itself is read-only.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
