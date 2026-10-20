## Description:

Ranks company leads against a user-defined ideal customer profile using Cargo firmographics, with a score, explanation, and tier for each qualified account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and revenue operations teams use this skill to enrich company domains, score leads against agreed firmographic criteria, and prioritize accounts for outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company domains are sent to Cargo for enrichment and may consume credits.

Mitigation: Confirm the user accepts third-party enrichment, sample 10–20 records, and obtain approval for the estimated full-run cost.

Risk: Setup can create a Cargo account, and the skill proposes a session-attribution action unrelated to lead scoring.

Mitigation: Ask before account creation and review or skip the attribution action.

Risk: The skill suggests starring a GitHub repository using the user's account.

Mitigation: Only star after the user explicitly agrees; skip the request if it is not relevant.

Risk: Installing the latest CLI version can introduce unreviewed changes.

Mitigation: Pin and review the CLI package version in controlled environments.

## Reference(s):

- [Score Leads on ClawHub](https://clawhub.ai/cargo-ai/skills/score-leads)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo ICP discovery recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/icp-discovery.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown table with scores, tiers, reasons, and missing fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports sample cost and score distribution; leaves accounts with missing firmographics unranked.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
