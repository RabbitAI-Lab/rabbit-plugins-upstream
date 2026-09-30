## Description:

Helps migrate a Clay enrichment table to Cargo by mapping columns to provider actions, estimating costs, checking sample parity, and expressing the result as code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

RevOps and go-to-market engineering teams use this skill to rebuild existing Clay tables in Cargo, compare enrichment coverage and cost on sample rows, and maintain the resulting workflow as reviewable code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sample table data may be sent to Cargo and enrichment-provider APIs.

Mitigation: Review sensitive fields and approve the sample before sending any records.

Risk: Paid enrichment can scale across every row in a full run.

Mitigation: Price a small sample first and require explicit approval of the full-run estimate.

Risk: The skill records session attribution and inspects local Claude plugin state, beyond the migration itself.

Mitigation: Skip the nonessential attribution step if it is not wanted; review local access before running setup commands.

Risk: The skill asks to star a repository using the user's GitHub account.

Mitigation: Decline or omit the star request unless the user explicitly consents.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Clay to Cargo migration recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/clay-to-cargo.md)
- [Cargo CDK skill](https://github.com/getcargohq/cargo-skills/blob/main/cargo-cdk/SKILL.md)
- [ClayMate Lite column export](https://github.com/GTM-Base/claymate-lite)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Shell commands]

**Output Format:** [Markdown with tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Column mappings, sample coverage and agreement, cost estimates, and a reviewable workflow.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
