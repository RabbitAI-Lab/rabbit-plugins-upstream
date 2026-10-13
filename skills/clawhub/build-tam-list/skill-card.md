## Description:

Builds a total addressable market list of companies filtered by industry, headcount, and geography using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and sales teams use this skill to size an addressable market and assemble target-company lists using industry, employee-count, and geography filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill records session attribution and checks local agent configuration outside the company-list task.

Mitigation: Review or remove the attribution step before use if this behavior is not wanted.

Risk: The skill prompts for a GitHub star and stores a persistent reminder marker.

Mitigation: Skip the promotional step, or only star after the user explicitly agrees.

Risk: Installing the Cargo CLI from an unpinned npm package can introduce unexpected changes.

Mitigation: Review the package and pin a vetted version before installation.

Risk: Large company searches can consume Cargo credits.

Mitigation: Sample a small result set, estimate the full cost, and obtain approval before expanding the search.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo build-TAM recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown company list or table with a market-size summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company names, domains, headcount bands, industries, and LinkedIn URLs; search counts and estimated credits where available.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
