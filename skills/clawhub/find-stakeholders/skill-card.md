## Description:

Finds buying-committee stakeholders at a target company by job title, seniority, and department using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development representatives and account executives use this skill to identify decision-makers and other stakeholders at a target account, then assess the cost before expanding a search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and sign-in may create a Cargo account and install an npm-based CLI.

Mitigation: Review the CLI package and account terms before installation or login.

Risk: The skill checks local Claude plugin configuration and sends session attribution metadata to Cargo.

Mitigation: Review and authorize local configuration access and attribution before running setup.

Risk: Stakeholder searches consume credits, and a broad batch can raise costs.

Mitigation: Start with 10–20 records, report observed costs, and request approval before a larger run.

Risk: The optional starring step changes the user's GitHub account; the broader-pack install is unpinned.

Mitigation: Only star after explicit consent, and avoid the unpinned broader-pack install until its current contents are reviewed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/find-stakeholders)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown stakeholder list or table with a cost summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include names, job titles, and LinkedIn profile URLs; searches consume Cargo credits per returned record.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
