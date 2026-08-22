## Description:

Read first when using any SentiSense stock market skill: API key setup and which skill owns each task. Patterns to adapt, not scripts. The user's task always wins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users start here when using the SentiSense stock-market skill collection to set up the shared API key, choose the narrowest matching SentiSense skill, and follow read-only market-data conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key.

Mitigation: Store SENTISENSE_API_KEY in the host credential store or environment and verify access with a cheap read-only call instead of printing the secret.

Risk: Market data and sentiment outputs may be mistaken for investment advice.

Mitigation: Present outputs as research or educational content, not financial advice, and keep the read-only boundary clear.

Risk: Preview responses or empty results can be overinterpreted.

Mitigation: State when a response is a preview or empty, and avoid filling missing market data from memory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API documentation](https://sentisense.ai/docs/api)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and routing tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the SENTISENSE_API_KEY environment-backed credential for read-only SentiSense market-data calls.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
