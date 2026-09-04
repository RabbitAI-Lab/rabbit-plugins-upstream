## Description:

Search and read public Groupon deal listings, deal details, and category taxonomy from the terminal with anonymous curl requests to Groupon's consumer GraphQL API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to browse Groupon offers, inspect deal details, and list category taxonomy without requiring credentials or a browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Groupon search terms, city slugs, and deal IDs are sent to Groupon during public deal lookup.

Mitigation: Avoid private information in search queries and use the skill only for anonymous public deal browsing, not purchasing or account actions.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with curl and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are agent-facing instructions and command snippets for anonymous public Groupon GraphQL reads; persisted query hashes may need refreshing if Groupon changes them.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
