## Description:

Compare cricket players and teams using Cricinfo statistics, records, scorecards, and rankings while preserving match format, dates, filters, and source context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Cricket analysts and other users compare players or teams within specified formats and date windows, with source-linked statistics, denominators, and caveats about incomplete or incomparable records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cricket lookup parameters and a Crawlora API key are sent to Crawlora, and queries may consume credits.

Mitigation: Use a key scoped to Crawlora, monitor API usage and credits, and limit requests to the documented Cricinfo endpoints and requested scope.

Risk: Comparisons may mislead if formats, denominators, table coverage, or overs notation differ.

Mitigation: Compare like-for-like records, retain source definitions and dates, and disclose truncated results or unknown values.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/crawlora-org/skills/cricket-player-team-comparison)
- [Cricinfo endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown comparison table and explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes entity and filter ledger, denominators and units, source context, missing values, and coverage limitations.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
