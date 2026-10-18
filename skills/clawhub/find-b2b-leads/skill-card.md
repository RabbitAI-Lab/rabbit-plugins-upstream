## Description:

Finds B2B prospects by role, company, and keyword and returns structured lead lists through Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development teams use this skill to source people matching target roles and companies for outbound prospecting, with LinkedIn profile links for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the Cargo CLI and signing in grants access to an external service that receives lead-search criteria.

Mitigation: Review the CLI and data-sharing requirements before installation or use in a work environment.

Risk: The skill checks local agent configuration and records Cargo session attribution unrelated to the lead results.

Mitigation: Review the configuration check and session attribution before running the skill; omit those steps if they are not approved.

Risk: The optional GitHub star flow acts on the user's account, and the optional full-pack install uses an unpinned package source.

Mitigation: Skip the star unless the user explicitly consents, and avoid the full-pack install unless its source is separately trusted.

Risk: Broad lead searches can consume credits, and unsupported filters may be ignored without warning.

Mitigation: Validate filter codes and sample a small search before approving a larger run and its estimated cost.

## Reference(s):

- [Find B2B Leads on ClawHub](https://clawhub.ai/cargo-ai/skills/find-b2b-leads)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured lead list or Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lead names, titles, companies, locations, and LinkedIn profile URLs; email addresses are not provided.]

## Skill Version(s):

1.2.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
