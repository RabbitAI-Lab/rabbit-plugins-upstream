## Description:

Use this skill for DealMachine searching and data retrieval through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search, count, and retrieve DealMachine property data, inspect available fields and filters, and check account or plan details through the OOMOL DealMachine connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read DealMachine account, property, people, filter, and search data through the connected OOMOL account.

Mitigation: Use only intended OOMOL and DealMachine accounts, and review connector responses before sharing enriched property or contact data.

Risk: Some searches or enrichments may consume DealMachine or OOMOL credits.

Mitigation: Inspect the live action schema and payload before execution, and use count or cost-estimation actions where available.

## Reference(s):

- [DealMachine homepage](https://dealmachine.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dealmachine)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect live connector schemas before running actions and to return connector results from the oo CLI.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
