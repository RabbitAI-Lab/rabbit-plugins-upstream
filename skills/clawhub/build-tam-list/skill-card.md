## Description:

Builds a list of companies matching industry, headcount, and geography filters using Cargo's Sales Navigator search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and revenue operations teams use this skill to find target accounts and estimate an addressable market from filtered company records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and authenticating the Cargo CLI and searching remote services may disclose account information and consume credits.

Mitigation: Review the service and access requirements first; sample a small list, check observed cost, and obtain approval before a full paid run.

Risk: Optional attribution, unpinned full-pack installation, and GitHub starring add side effects unrelated to the company search.

Mitigation: Skip those optional actions unless the user explicitly requests them; the core company search does not require a GitHub star.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/build-tam-list)
- [Cargo GTM skills homepage (listed in skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Cargo build-TAM recipe (linked in skill instructions)](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown company list or table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company records can include name, domain, headcount band, industry, and LinkedIn URL; results do not include a total match count.]

## Skill Version(s):

1.2.1 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
