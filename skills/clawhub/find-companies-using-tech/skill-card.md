## Description:

Helps sales and marketing teams find companies using specified technologies or hiring for specified roles through Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and marketing teams use this skill to identify companies by technology stack and recent job postings, with evidence for each match.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches consume credits, and unrecognized filters may silently broaden paid results.

Mitigation: Check filter keys, test on 10–20 records, and approve the estimated cost before a full run.

Risk: CLI login and session attribution associate activity with a Cargo account.

Mitigation: Review account login and session attribution before running the skill.

Risk: The optional GitHub star action uses the user's authenticated account.

Mitigation: Do not star the repository without the user's explicit approval.

Risk: The suggested full-pack install uses an unpinned package reference.

Mitigation: Avoid that optional install unless the source and current package contents are trusted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/find-companies-using-tech)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo tech-intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown summary and company table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes matching technology and hiring evidence when available.]

## Skill Version(s):

1.1.3 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
