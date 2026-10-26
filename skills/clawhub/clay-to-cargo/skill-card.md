## Description:

Helps migrate a Clay enrichment table to Cargo by mapping columns to provider actions, testing cost and coverage, and expressing the resulting workflow as code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM engineers and revenue operations teams use this skill to migrate existing Clay tables to Cargo, compare sample enrichment results and costs, and keep the workflow reviewable as code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clay and Cargo records may be shared with Cargo and its connector providers.

Mitigation: Use only data approved for those services and begin with a small sample.

Risk: A full enrichment batch can incur substantial credit charges.

Mitigation: Report sample costs and require explicit approval of the full row count and estimate.

Risk: The skill includes Cargo session attribution and checks local Claude plugin state.

Mitigation: Review these steps before installation and avoid this skill if the tracking or local check is unacceptable.

Risk: The skill can prompt for a GitHub star and use the user's GitHub account to create it.

Mitigation: Only take the action after the user explicitly agrees; otherwise skip it.

## Reference(s):

- [Skill page](https://clawhub.ai/cargo-ai/skills/clay-to-cargo)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Complete Clay-to-Cargo migration recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/clay-to-cargo.md)
- [Cargo project skill](https://github.com/getcargohq/cargo-skills/blob/main/cargo-project/SKILL.md)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with tables and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sample cost, coverage, and column-parity comparisons; reviewable workflow configuration.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
