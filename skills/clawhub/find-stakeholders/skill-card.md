## Description:

Find the buying committee at a target account — every stakeholder matching a set of titles, seniorities, and departments, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and account teams use this skill to identify decision makers and other buying committee members at a target company. They can filter a stakeholder search by title, seniority, and department, then use the results to plan account outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stakeholder searches send company domains and filters to Cargo/aiArk and consume credits.

Mitigation: Use only intended company domains and filters; sample a small result set, report observed cost, and get approval before a larger run.

Risk: The installed CLI, optional broader pack, and linked external recipe were not included in the security review.

Mitigation: Review dependency versions and relevant code before installing the CLI or optional pack.

Risk: The optional GitHub star changes the user's account state.

Mitigation: Ask for explicit permission and star the repository only after the user agrees.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/find-stakeholders)
- [Cargo GTM skills homepage (listed in skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Account expansion recipe (linked from skill documentation)](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Structured data]

**Output Format:** [Markdown guidance with shell commands and stakeholder result records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include names, titles, seniority, department, and profile links; record volume affects credit use.]

## Skill Version(s):

1.0.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
