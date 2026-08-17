## Description:

Finds stakeholders in a target account by matching titles, seniorities, and departments through Cargo's aiArk people-search provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, and go-to-market teams use this skill to identify buying-committee stakeholders at a specific target account before outreach or account expansion work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Cargo CLI stores login state and uses Cargo and aiArk for B2B people search.

Mitigation: Install and authenticate only when that external service use and local login state are acceptable for the workspace.

Risk: Larger searches can consume credits for each returned stakeholder record.

Mitigation: Confirm the target account and expected record count first, then sample before running larger searches.

## Reference(s):

- [Cargo GTM Skills](https://github.com/getcargohq/gtm-skills)
- [Cargo Account Expansion Recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash commands and structured CLI output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses asynchronous Cargo CLI operations and credit-based people-search results.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
