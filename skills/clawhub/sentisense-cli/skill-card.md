## Description:

Guides agents in retrieving US stock quotes, sentiment, analyst data, trading disclosures, institutional flows, options positioning, and screening results through SentiSense's read-only CLI or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to obtain read-only US stock market data and incorporate quotes, sentiment, disclosures, and screening results into answers or scripts. The data is informational, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the suggested npm CLI downloads and executes code with access to the SentiSense API key.

Mitigation: Confirm with the user before first execution, verify the package and publisher, and prefer the documented REST path when a shell command is unnecessary.

Risk: An API key could be exposed to an unintended service or through command-line arguments.

Mitigation: Pass the key through SENTISENSE_API_KEY rather than arguments, and keep requests directed to https://app.sentisense.ai.

Risk: Market data and generated sentiment can be mistaken for personalized investment advice.

Mitigation: Present results as informational data and leave investment decisions to the user.

## Reference(s):

- [SentiSense API reference and REST alternative](https://sentisense.ai/skill.md)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/sentisense-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Guidance]

**Output Format:** [Markdown with bash examples and REST guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggested commands return plain text or JSON; stable exit codes distinguish success, usage, authentication, missing data, limits, and network failures.]

## Skill Version(s):

0.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
