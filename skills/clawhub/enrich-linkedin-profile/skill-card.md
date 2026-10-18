## Description:

Enriches LinkedIn profile URLs with person details and verified work email addresses through Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and account teams use existing LinkedIn profile URLs to obtain contact profiles and verified work emails for prospecting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn profile URLs are sent to Cargo and aiArk for enrichment.

Mitigation: Use only URLs you are authorized to process and review data-sharing requirements before running the skill.

Risk: The workflow uses a persistent Cargo login and includes non-essential session tracking and access to local agent configuration.

Mitigation: Review optional session actions and the account permissions before execution; skip non-essential tracking.

Risk: The skill suggests an unpinned full-pack install and an unrelated GitHub starring action.

Mitigation: Avoid the separate installation and starring steps unless explicitly requested and approved.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)
- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/enrich-linkedin-profile)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Contact records or Markdown tables with profile details and work emails]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records without a verified email return no profile data; successful enrichments consume credits.]

## Skill Version(s):

1.1.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
