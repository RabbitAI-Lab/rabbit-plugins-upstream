## Description:

Find the buying committee at a target account by searching for stakeholders who match selected titles, seniorities, and departments, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business development teams use this skill to find likely buying committee members at a target account, filtering by role, seniority, and department. It returns stakeholder records for review and follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches share target-company and role filters with Cargo and aiArk, and consume service credits.

Mitigation: Confirm the filters are appropriate to share, sample a small search, report its cost and hit rate, and get approval before a larger run.

Risk: The downloaded CLI and optional broader skill pack are outside the provided security review.

Mitigation: Review or pin the CLI and broader pack separately before use.

## Reference(s):

- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, API Calls]

**Output Format:** [Markdown instructions and stakeholder records, with title, seniority, and department details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results depend on the selected filters and service availability; the skill describes credit-based search costs.]

## Skill Version(s):

1.0.4 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
