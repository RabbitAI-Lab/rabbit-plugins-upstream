## Description:

Guides agents through counting, splitting, and recombining oversized Sales Navigator searches for account or people extraction with Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development, revenue operations, and GTM teams use this skill to plan and execute large Sales Navigator account or people searches that exceed per-search extraction limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo authentication and extraction may send Sales Navigator search URLs and results to Cargo.

Mitigation: Review the data-sharing implications and obtain approval before signing in or extracting results.

Risk: The skill reads agent configuration and records session attribution beyond the extraction task.

Mitigation: Review and omit the attribution step unless it is explicitly authorized.

Risk: The skill offers to star a repository using the user's GitHub account.

Mitigation: Do not perform the public GitHub action unless the user explicitly requests it.

Risk: Installing the Cargo CLI from an unpinned latest release can change the code executed.

Mitigation: Prefer a reviewed, pinned package version before running installation commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/extract-sales-navigator-search)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and Sales Navigator search URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search counts, extraction planning, credit estimates, and deduplication guidance.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
