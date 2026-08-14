## Description:

Builds a total addressable market list of companies filtered by industry, headcount, and geography, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and go-to-market operators use this skill to size a company account market and generate a targeted TAM list from industry, headcount, and geography filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires installing and using Cargo's CLI and signing into a Cargo workspace.

Mitigation: Install only when the user accepts Cargo CLI use and workspace authentication for this task.

Risk: The workflow can query Sales Navigator account data through Cargo.

Mitigation: Review the intended filters, account context, and limit before executing a search.

Risk: Credit usage can scale with larger account searches.

Mitigation: Start with a small sample, report observed cost and hit rate, then get approval with a record count and credit estimate before a larger run.

## Reference(s):

- [Cargo GTM Skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo build TAM recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/build-tam-list)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides setup, authentication, TAM search parameters, asynchronous run polling, and credit-aware sampling before larger runs.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
