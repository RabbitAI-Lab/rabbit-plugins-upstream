## Description:

Query booli.se property data from a shell with the fpx CLI, including area lookup, for-sale listings, sold listings, and property details through one-shot GraphQL calls routed through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to retrieve public Booli property data from scripts or shell workflows without running the booli MCP server. It is useful for resolving Swedish area IDs, searching active or sold listings, and fetching property details for downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paired browser-assisted CLI profile can inherit browser session context if used carelessly.

Mitigation: Keep the fpx profile limited to booli.se, use only the fetch capability, and avoid using an unnecessary logged-in Booli session.

Risk: Automated property queries may conflict with Booli usage terms or rate expectations.

Mitigation: Use the skill for read-only public queries, keep request volume reasonable, and confirm the workflow fits booli.se's terms.

## Reference(s):

- [Booli GraphQL query recipes](artifact/references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with shell commands and JSON GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs GraphQL JSON responses suitable for jq processing; users should check GraphQL errors even when the HTTP request succeeds.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
