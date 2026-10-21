## Description:

Finds work email addresses from a person's name and company domain using Cargo's email-enrichment providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and revenue operations teams use this skill to find work emails for contacts with a known name and company domain, leaving unmatched contacts blank.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact records are sent to external email-enrichment providers.

Mitigation: Submit only contact data approved for sharing with Cargo and its enrichment providers.

Risk: Large batches consume credits, and the CLI requires authentication.

Mitigation: Review authentication requirements; sample 10–20 records, estimate the credit cost, and obtain approval before a full batch.

Risk: The skill requests a GitHub star and writes a local marker unrelated to finding emails.

Mitigation: Decline or remove the starring step and local marker when only email finding is wanted; never star without explicit user consent.

Risk: A workspace attribution action reports use of the standalone skill to Cargo.

Mitigation: Review and omit the attribution action if that reporting is not acceptable.

Risk: Installation uses an unpinned CLI package version.

Mitigation: Review the package and pin a vetted version before installation.

## Reference(s):

- [Cargo GTM skills homepage (linked in skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe (linked in skill)](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Contact-by-contact work email results, optionally as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unresolved contacts remain blank rather than receiving guessed addresses.]

## Skill Version(s):

1.1.2 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
