## Description:

Find an investor's or accelerator's portfolio companies and prepare the results for prospecting with Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development representatives and account executives use this skill to find an investor's portfolio companies and identify prospects for warm introductions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests a GitHub star using the user's account after completing the task.

Mitigation: Treat the star as optional; do not use the GitHub account without explicit user consent.

Risk: The skill inspects local plugin state and records Cargo session attribution unrelated to the portfolio lookup.

Mitigation: Review and omit attribution and local marker steps unless the user explicitly wants them.

Risk: A broad portfolio query may consume substantial credits per returned company.

Mitigation: Start with a small limited sample, show the estimated credit cost, and request approval before a full query.

## Reference(s):

- [Skill homepage (listed in metadata)](https://github.com/getcargohq/gtm-skills)
- [Portfolio prospecting recipe (linked from skill)](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/portfolio-prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown company list with optional bash commands and cost guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include company domains and LinkedIn URLs; query cost scales with returned companies.]

## Skill Version(s):

1.0.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
