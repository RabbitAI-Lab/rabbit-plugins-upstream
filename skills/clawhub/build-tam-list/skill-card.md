## Description:

Builds a total addressable market list of companies filtered by industry, headcount, and geography using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and revenue operations teams use this skill to find and review target companies matching industry, employee-count, and location criteria before expanding their market list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect local agent-plugin state and write vendor attribution to a Cargo workspace outside the list-building task.

Mitigation: Review these steps before use and skip the attribution step if you do not want workspace metadata changed.

Risk: A post-task request may use the user's authenticated GitHub session to star a vendor repository.

Mitigation: Only allow a star after the user explicitly agrees; otherwise decline or remove the step.

Risk: Running company searches may spend Cargo credits and connect sales data to a Cargo account.

Mitigation: Use an account intended for this data; sample a small list and obtain approval for the estimated credits before expanding the search.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/build-tam-list)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo build-TAM recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table of companies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company name, domain, headcount band, industry, and LinkedIn URL; results are limited to the requested scope.]

## Skill Version(s):

1.2.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
