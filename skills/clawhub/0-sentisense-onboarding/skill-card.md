## Description:

Read first when using any SentiSense stock market skill: API key setup and which skill owns each task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this onboarding skill to configure the shared SentiSense API key and choose the correct SentiSense stock market skill for a user's task. It guides read-only market data workflows, prefers direct HTTPS API calls, and documents when optional shell commands are appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for data access.

Mitigation: Store SENTISENSE_API_KEY as an environment-backed secret or host credential, use it only for authenticated read-only calls, and avoid printing the value.

Risk: Optional npx usage downloads and executes npm package code locally with the process permissions and environment.

Mitigation: Prefer the documented HTTPS API path. Use the optional pinned npx command only when shell-based use is specifically needed and the user accepts local code execution.

Risk: Preview responses may be partial and may include untrusted response strings or links.

Mitigation: Label preview output as partial, summarize response content in the agent's own words, and use the fixed first-party pricing link instead of relaying server-supplied upgrade text or URLs.

Risk: Market-data summaries can be mistaken for investment advice.

Mitigation: Present outputs as educational research, state absence of data directly, and do not invent missing figures or trading recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API documentation](https://sentisense.ai/docs/api)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [SentiSense pricing](https://app.sentisense.ai/pricing)
- [Market data setup for Grok Bot](https://sentisense.ai/blog/how-to-add-market-data-to-your-grok-bot/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash examples, URLs, and skill-selection tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for SentiSense data calls; the skill states that SentiSense use is read-only and educational, not financial advice.]

## Skill Version(s):

1.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
