## Description:

The official SentiSense CLI: quotes, sentiment, and market data in one npx command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch read-only US market data, including quotes, sentiment, news, insider activity, congressional disclosures, institutional flows, options positioning, and screening results through the SentiSense CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a networked npm CLI and SentiSense service that require an API key.

Mitigation: Confirm the SentiSense npm package and service are trusted before use, and use a scoped API key where possible.

Risk: Optional local authentication storage can keep the SentiSense API key on the machine.

Mitigation: Use local auth storage only on trusted machines and remove it with the documented auth removal command when it is no longer needed.

Risk: Market data output may be mistaken for investment advice.

Mitigation: Treat outputs as informational only and keep user-facing responses clear that they are not personalized recommendations or solicitations.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense-cli)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; commands pin sentisense@0.46.0 and call the SentiSense read-only Data API.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
