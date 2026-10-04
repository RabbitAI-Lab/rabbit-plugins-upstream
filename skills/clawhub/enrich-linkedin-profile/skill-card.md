## Description:

Enriches LinkedIn profile URLs with professional details and available verified work emails through Cargo and aiArk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development representatives and account executives use LinkedIn profile URLs to obtain professional background and available verified work emails for prospecting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unpinned Cargo CLI may introduce unexpected changes.

Mitigation: Review the package and pin an approved version before installation.

Risk: Enrichment sends LinkedIn profile data to Cargo and aiArk.

Mitigation: Confirm authorization and data-handling requirements before submitting profiles.

Risk: The skill includes session attribution and a request to star the publisher's repository unrelated to enrichment.

Mitigation: Omit attribution if not wanted, and never star a repository without explicit user consent.

Risk: Large batches can consume credits unexpectedly.

Mitigation: Trial a small batch and obtain approval for the estimated full-run cost.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)
- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/enrich-linkedin-profile)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with bash examples and tabular profile results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile and email coverage varies; batch enrichment may incur per-result credits.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
