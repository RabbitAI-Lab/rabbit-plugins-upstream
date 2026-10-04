## Description:

Scores and ranks companies against a user-defined ideal customer profile, showing the score, reasoning, tier, and missing data for each account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and revenue operations teams use this skill to prioritize a supplied list of company domains against an agreed customer profile. It enriches needed firmographics, then produces explainable, tiered rankings while leaving records with missing data unranked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vendor attribution records a session beyond the lead-scoring task.

Mitigation: Review and explicitly approve attribution before running the optional session command.

Risk: An optional larger-pack installer is not version-pinned, and the skill checks local agent configuration.

Mitigation: Review local configuration access and install the larger pack only if needed, using a reviewed, pinned version.

Risk: The skill offers to star a GitHub repository using the user's account.

Mitigation: Treat starring as optional and require explicit user approval before any account action.

Risk: Company enrichment consumes credits across every processed record.

Mitigation: Start with a small sample, disclose observed costs, and obtain approval for the full batch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/score-leads)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo ICP discovery recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/icp-discovery.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown table with scores, tiers, reasons, missing fields, and cost summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sample scoring and cost estimate before approval for a full paid enrichment run.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
