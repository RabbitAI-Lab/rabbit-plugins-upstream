## Description:

Read first when using any SentiSense stock market skill: API key setup and which skill owns each task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this onboarding skill to configure SentiSense API access and choose the right SentiSense stock-market skill for a task. It helps agents provide research-oriented market workflows while keeping the user's request in control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat stock-market outputs as financial advice.

Mitigation: Present outputs as research or educational information and avoid recommending trades as instructions.

Risk: The required SentiSense API key could be exposed if handled carelessly.

Mitigation: Use the SENTISENSE_API_KEY environment-backed secret and do not print or log the key value.

Risk: Preview or empty data responses could be misread as complete market coverage.

Mitigation: State preview status or empty results plainly and do not fill gaps with unsourced values.

Risk: Free-key rate limits may affect completeness or freshness of multi-call workflows.

Mitigation: Page requests serially, honor Retry-After on rate-limit responses, and summarize any missing data caused by limits.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Documentation](https://sentisense.ai/docs/api)
- [SentiSense API Key Setup](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for SentiSense data access; documented behavior is read-only and educational, not financial advice.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
