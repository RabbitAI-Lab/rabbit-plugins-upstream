## Description:

Find a verified work email address from a person's name and company domain, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and RevOps teams use this skill to find verified work email addresses for contacts from their names and company domains, including prospect lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact records may contain information the user does not want to share with Cargo, Prospeo, or FullEnrich.

Mitigation: Use only contact records the user is comfortable sharing with those providers.

Risk: Large batches can incur credit costs across every submitted record.

Mitigation: Sample 10–20 records, review the observed cost and hit rate, then approve a full batch only after seeing the record count and credit estimate.

## Reference(s):

- [Cargo GTM Skills project](https://github.com/getcargohq/gtm-skills)
- [ClawHub find-work-email release](https://clawhub.ai/cargo-ai/skills/find-work-email)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Contact records with verified work email addresses, typically presented as a Markdown table; unresolved rows remain empty.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One result per contact; unresolved email fields are left blank rather than guessed.]

## Skill Version(s):

1.1.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
