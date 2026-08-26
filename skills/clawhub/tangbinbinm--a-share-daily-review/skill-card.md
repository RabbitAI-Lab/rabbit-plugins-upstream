## Description:

Generates a fact-only daily global market review for A-shares, Hong Kong, U.S., Asia-Pacific, Europe, and north-bound capital flow using public akshare data without API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangbinbinm](https://clawhub.ai/user/tangbinbinm)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to generate a structured, fact-only daily market report from public market data. It is intended for market-data reporting and copy-friendly summaries, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run for broad market-review requests and make outbound requests to public market-data providers through akshare.

Mitigation: Review when the skill activates, and use it only where outbound access to public market-data providers is acceptable.

Risk: Market summaries could be mistaken for investment advice.

Mitigation: Keep outputs fact-only, include the required disclaimer, and avoid buy, sell, recommendation, or prediction language.

Risk: Public market-data sources may be unavailable, delayed, or partially missing.

Mitigation: Report unavailable sections and data-quality errors instead of filling gaps with inferred values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tangbinbinm/skills/a-share-daily-review)
- [artifact/README.md](artifact/README.md)
- [artifact/SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured Markdown report or plain text summary, backed by JSON data from the local script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs fact-only market summaries, deterministic insights, data-quality notes, and a required investment-advice disclaimer.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
