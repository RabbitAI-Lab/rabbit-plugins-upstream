## Description:

Finds B2B prospects by job title, company, and keyword and returns a structured lead list through Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development teams use this skill to source people matching title, company, industry, and location criteria for outbound prospecting. It returns profiles and LinkedIn URLs, not email addresses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using Cargo creates a persistent third-party workspace and shares lead-sourcing activity with the service.

Mitigation: Install and sign in only if the user accepts Cargo as a lead-sourcing service and understands the workspace will persist.

Risk: Paid searches and larger batches can spend credits.

Mitigation: Start with a small sample, report observed cost and match rate, and get approval for the estimated full-run cost.

Risk: The skill checks local agent configuration and records vendor attribution outside the core sourcing task.

Mitigation: Review and approve those additional actions before running setup commands.

Risk: The optional GitHub starring flow can use the user's account for vendor promotion.

Mitigation: Do not star the repository unless the user explicitly opts in; decline the request otherwise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/find-b2b-leads)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands]

**Output Format:** [Structured lead list or Markdown table with CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lead profiles include names, titles, companies, and LinkedIn URLs; no email addresses are returned by sourcing.]

## Skill Version(s):

1.2.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
