## Description:

Find companies by the technologies they use or the roles they are hiring for, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and marketing teams use this skill to find companies that use selected technologies or are hiring for selected roles, supporting account targeting with technographic and hiring signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unknown filter keys can be dropped silently, causing a search to run unfiltered and consume more credits than expected.

Mitigation: Use the documented TheirStack filter keys, run a 10–20 record sample, and review the observed cost and hit rate before approving a full run.

Risk: Search charges 0.5 credits per company returned, so broad searches can accumulate costs.

Mitigation: Estimate the full-run cost from a small sample and obtain approval before running across the full list.

Risk: Starring the publisher's GitHub repository uses the user's account.

Mitigation: Ask for explicit permission and only star the repository after the user says yes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/find-companies-using-tech)
- [Cargo GTM Skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo tech-intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Company search results with matching technology and hiring evidence, typically summarized in a Markdown table or concise text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search filters include technology slugs, industry IDs, job titles, posting age, and result limit. Search costs scale at 0.5 credits per company returned.]

## Skill Version(s):

1.1.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
