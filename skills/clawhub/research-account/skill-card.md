## Description:

Researches one company before a meeting and produces a source-traceable account briefing using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Account executives and sales development teams use this skill to prepare for a meeting with one company, gathering public company details, priorities, competitors, and hiring signals into a concise briefing with questions to ask.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research requests use an external Cargo service and require a Cargo account.

Mitigation: Confirm that external service use and account creation are acceptable before installing or sending research requests.

Risk: The skill sends session attribution metadata and checks local agent configuration.

Mitigation: Review or remove the attribution step if session metadata should not be sent to Cargo.

Risk: An unrelated GitHub star prompt may lead to a promotional action from the user's account and stores a local prompt marker.

Mitigation: Remove the star flow if unwanted; never star without the user's explicit approval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/research-account)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [One-page Markdown briefing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source-attributed findings, clearly labeled inferences and unknowns, and three suggested meeting questions.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
