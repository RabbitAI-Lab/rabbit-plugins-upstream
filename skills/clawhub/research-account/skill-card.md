## Description:

Research one company and its public website before a meeting, then prepare a source-traceable briefing on what it does, its publicly stated challenges, and its named competitors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and account teams use this skill to prepare for a meeting with one company by reviewing public company information, stated priorities and challenges, competitors, and hiring signals, then producing a concise sourced briefing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research actions send company-related requests to external services and consume Cargo credits.

Mitigation: Review the requested sources and estimated credit use before execution; sample a small set before researching a full list.

Risk: The installation command uses @cargo-ai/cli@latest, and the optional broader pack contains code that is not bundled with this skill.

Mitigation: Review package versions and the broader pack before enabling them.

Risk: The skill may ask the user to star a GitHub repository and can create a local marker recording that it asked.

Mitigation: Only star after explicit user approval; review the marker behavior if needed.

## Reference(s):

- [Cargo GTM Skills homepage (listed by the skill)](https://github.com/getcargohq/gtm-skills)
- [Account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)
- [ClawHub release page](https://clawhub.ai/cargo-ai/skills/research-account)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [One-page Markdown company briefing with source-attributed claims, labeled inferences, stated unknowns, and meeting questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Claims are traceable to sources; inferences are marked Likely and unsupported information is identified as unknown.]

## Skill Version(s):

1.0.4 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
