## Description:

Resolve a person's LinkedIn profile URL from their name and company, with a validation step that rejects wrong matches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, recruiting, and go-to-market operators use this skill to add validated LinkedIn profile URLs to contact records from a person's name and company. It is intended for single-contact lookups and approved batch enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact identity data is sent through Cargo's CLI and LinkedIn connector during lookup and validation.

Mitigation: Confirm the user is comfortable using Cargo and sending contact identity data before running the workflow.

Risk: Batch lookups consume Cargo credits and cost scales with record count.

Mitigation: Run a small sample first, report observed cost and hit rate, and get approval for the estimated full-batch cost.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/find-linkedin-url)
- [Cargo GTM Skills Homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo LinkedIn URL Lookup Recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/linkedin-url-lookup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command blocks and JSON command payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces validated LinkedIn URL lookup guidance; unresolved rows are marked explicitly.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
