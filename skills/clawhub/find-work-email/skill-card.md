## Description:

Finds verified work email addresses from a person's name and company domain using Cargo, with prospeo first and FullEnrich for unresolved contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM teams, sales operators, and agents use this skill to find work email addresses for individual contacts or prospect lists from a name and company domain. It supports cost-controlled enrichment by sampling first, using the cheaper provider first, and escalating only unresolved contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact enrichment can consume credits quickly when run across a full list.

Mitigation: Start with a 10-20 record sample, report observed hit rate and credit cost, then ask for explicit approval before full-list processing.

Risk: The workflow sends contact data to Cargo and its disclosed enrichment providers.

Mitigation: Install and use the skill only when the user is comfortable with Cargo and its enrichment providers handling the contact data.

Risk: Running both enrichment providers across all records can duplicate cost.

Mitigation: Run prospeo first across the target records and escalate only unresolved contacts to FullEnrich.

## Reference(s):

- [Cargo GTM Skills Repository](https://github.com/getcargohq/gtm-skills)
- [Cargo Prospecting Recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)
- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/find-work-email)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Cargo CLI workflow guidance and provider selection steps; unresolved contacts are left empty rather than guessed.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
