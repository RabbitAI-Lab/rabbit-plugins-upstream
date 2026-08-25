## Description:

Stand up an account universe as a deployed Cargo CDK pipeline by splitting oversized Sales Navigator company searches, resolving companies to domains, and deduping them into a shared accounts model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM operators use this skill to adapt and deploy a Cargo CDK example that builds a market account list from Sales Navigator searches, splits searches that exceed extractor limits, and promotes resolved companies into an accounts table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The pipeline can spend Cargo credits during company promotion and enrichment.

Mitigation: Review the generated plan, start with a small counted sub-search, and widen only after costs and landed rows are acceptable.

Risk: Deploying the resources can mutate the shared accounts model.

Mitigation: Inspect the Cargo CDK plan and deploy only after explicit approval of the account-table changes.

Risk: Oversized or uncounted Sales Navigator searches can produce truncated account coverage.

Mitigation: Count each search, split any search at or above the extraction cap, and keep every configured sub-search below the limit before extraction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/tam-building)
- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Ark enrichment API](https://ai-ark.com/platform/enrichment-api)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with TypeScript CDK resources and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces adaptation, validation, and deployment guidance for a Cargo CDK workspace; generated plans should be reviewed before deployment.]

## Skill Version(s):

0.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
