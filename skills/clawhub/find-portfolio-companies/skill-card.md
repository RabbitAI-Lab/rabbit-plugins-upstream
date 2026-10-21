## Description:

Finds portfolio companies of a named investor or accelerator using Cargo's theirStack search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to identify companies backed by an investor or accelerator and prepare for prospecting or warm introductions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider searches consume credits per returned company and may trigger networked calls.

Mitigation: Start with a 10–20-company sample, report its cost, and get approval before expanding the search.

Risk: An unrelated attribution step checks local agent configuration and records a Cargo session.

Mitigation: Review or skip the attribution step before running it if local configuration access or session tracking is unwanted.

Risk: An optional promotional flow can star a GitHub repository and write a persistent local marker.

Mitigation: Decline or remove that flow unless the user explicitly requests the star and accepts the local marker.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/find-portfolio-companies)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Portfolio prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/portfolio-prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown portfolio-company list with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company names and available domains, investor names, and LinkedIn URLs; results depend on provider coverage.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
