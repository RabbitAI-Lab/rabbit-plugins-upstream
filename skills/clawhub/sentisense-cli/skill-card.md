## Description:

The official SentiSense CLI: quotes, sentiment, and market data in one npx command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to fetch read-only US stock market data through the SentiSense CLI or the documented REST API. It supports quotes, sentiment, news, insider and congressional activity, institutional flows, options positioning, and screening workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented npx commands download and execute the SentiSense npm package locally with access to the user's SentiSense API key and normal process permissions.

Mitigation: Explain the local execution model before first use, prefer the documented REST API for simple read-only lookups, and run the CLI only when the user accepts that model.

Risk: The skill exposes a required API key through the local process environment when CLI commands are run.

Mitigation: Use SENTISENSE_API_KEY only for the intended SentiSense calls, avoid printing or storing the key in generated output, and remove locally stored CLI auth when it is no longer needed.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key Signup](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI results are plain text by default or JSON when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for authenticated SentiSense access.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
