## Description:

Creates a source-traceable, one-page company briefing for meeting preparation using public company information, stated priorities, competitors, and hiring signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Account executives and sales development teams use this skill to prepare for a company meeting with a concise, sourced briefing and three tailored questions. The workflow distinguishes sourced facts, reasoned inferences, and information that could not be found.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo receives setup or session attribution and the skill checks local agent plugin state.

Mitigation: Review the setup steps and consent to attribution and the local-state check before running them.

Risk: Installing the latest Cargo CLI can introduce unreviewed dependency changes.

Mitigation: Review the package and pin a trusted version before installing.

Risk: The skill may prompt for a public GitHub star using the user's account.

Mitigation: Treat the star as optional; authorize it explicitly or decline it.

Risk: Research calls consume credits, and unbounded batch use can increase costs.

Mitigation: Estimate costs, cap job results, and get approval before running a full list.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [One-page text or Markdown briefing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source attribution, clearly labeled inferences and unknowns, and three tailored meeting questions.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
