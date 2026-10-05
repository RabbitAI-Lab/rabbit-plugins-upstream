## Description:

Finds stakeholders at a target account by job title, seniority, and department using Cargo's aiArk search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development representatives and account executives use this skill to identify a target account's buying committee by filtering people by seniority, department, and other job criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unpinned CLI package and signing in to Cargo introduces software and account-access exposure.

Mitigation: Review the CLI before installation, prefer a vetted pinned package version, and authorize account creation and sign-in.

Risk: Company and people-search data are sent through Cargo and aiArk; searches consume Cargo credits.

Mitigation: Confirm data-sharing suitability, sample 10–20 records, report observed costs, and obtain approval before larger runs.

Risk: The skill includes session attribution and a GitHub star request unrelated to finding stakeholders.

Mitigation: Consider skipping session attribution and the star request; never star without the user's explicit consent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/find-stakeholders)
- [Cargo GTM skills repository (listed homepage)](https://github.com/getcargohq/gtm-skills)
- [Cargo account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table or text list of matching stakeholders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes names, titles, seniority, and departments; report observed credit costs before expanding a search.]

## Skill Version(s):

1.0.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
