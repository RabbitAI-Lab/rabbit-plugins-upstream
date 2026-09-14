## Description:

Read first when using any SentiSense stock market skill: API key setup and which skill owns each task. Patterns to adapt, not scripts. The user's task always wins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill as the starting point for SentiSense stock market skills: it explains API-key setup, identifies which sibling skill fits a market-data task, and states shared read-only usage conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SentiSense API key for read-only SentiSense requests.

Mitigation: Keep SENTISENSE_API_KEY in the host credential store and avoid printing or copying the key into chat or logs.

Risk: Market-data outputs may be mistaken for investment advice.

Mitigation: Present outputs as research and educational content, and avoid trade instructions or claims of financial advice.

Risk: Preview responses may omit paid-plan data.

Mitigation: State when data is a free preview slice and do not present partial results as complete.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Key Setup](https://app.sentisense.ai/get-api-key)
- [SentiSense Full API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Documentation](https://sentisense.ai/docs/api)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)
- [Publisher Profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands, task-routing tables, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for SentiSense API use; outputs are educational market research guidance, not financial advice.]

## Skill Version(s):

1.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
