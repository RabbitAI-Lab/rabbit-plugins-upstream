## Description:

Use this onboarding skill to set up a SentiSense API key and choose the right read-only SentiSense stock-market skill for a user task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill as the entry point for the SentiSense stock-market skill collection: it explains API-key setup, shared credential handling, and which read-only market-data skill to open for each task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only market-data access.

Mitigation: Store SENTISENSE_API_KEY as an environment-backed secret or host-managed credential, and avoid printing or duplicating the key.

Risk: Market-data outputs may be partial when an API response indicates a preview dataset.

Mitigation: Tell the user when isPreview is true and avoid presenting partial data as a complete result.

Risk: Users may mistake market research output for financial advice.

Mitigation: Frame outputs as research and educational content, not trading instructions or financial advice.

Risk: Requests can hit SentiSense rate limits.

Mitigation: Page requests serially and honor Retry-After when the API returns 429.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense full API reference](https://sentisense.ai/skill.md)
- [SentiSense API documentation](https://sentisense.ai/docs/api)
- [Grok Bot setup guide](https://sentisense.ai/blog/how-to-add-market-data-to-your-grok-bot/)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and routing tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for SentiSense API access; outputs are educational and read-only.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
