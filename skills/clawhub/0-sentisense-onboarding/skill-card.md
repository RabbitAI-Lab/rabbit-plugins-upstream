## Description:

Introduces SentiSense stock market skills, explains API key setup, and routes users to the appropriate read-only market-data skill for a task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this onboarding skill to configure a SentiSense API key and choose the correct SentiSense market-data skill for a stock research task. It emphasizes read-only educational use and adapting patterns to the user's request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only market-data requests.

Mitigation: Install only when sharing this credential with SentiSense skills is acceptable, and store the key as an environment-backed secret rather than exposing it in outputs.

Risk: Free preview responses may be incomplete and may mention SentiSense pricing for full datasets.

Mitigation: Tell users when data is a preview, avoid presenting partial data as complete, and keep any pricing reference neutral and first-party.

Risk: Market-data outputs can be mistaken for financial advice.

Mitigation: Frame outputs as research and educational content, and avoid instructions to trade, move money, or treat absent data as known facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API documentation](https://sentisense.ai/docs/api)
- [SentiSense pricing](https://app.sentisense.ai/pricing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and routing tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only setup and routing guidance; no files, shell access, or write actions are required by the skill.]

## Skill Version(s):

1.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
