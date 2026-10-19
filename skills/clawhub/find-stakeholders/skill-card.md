## Description:

Finds buying-committee contacts at a target company using filters for role, seniority, and department through Cargo's aiArk search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and account teams use this skill to identify stakeholders at a target account and plan buying-committee outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill adds session attribution to a remote Cargo workspace beyond the stakeholder search.

Mitigation: Review the attribution step and omit it if only stakeholder discovery is needed.

Risk: The optional GitHub star request is unrelated to stakeholder discovery and can act on the user's account.

Mitigation: Skip the star workflow unless the user explicitly approves it.

Risk: External searches use Cargo and aiArk and can consume credits as results scale.

Mitigation: Review account data before sharing it and start with a small sample; obtain approval before a larger paid run.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/find-stakeholders)
- [Cargo skill homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown stakeholder list with names, titles, and profile links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected account, search filters, and returned records.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
