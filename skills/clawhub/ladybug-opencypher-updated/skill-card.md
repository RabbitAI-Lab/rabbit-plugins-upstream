## Description:

Designs and queries LadybugDB graphs with openCypher. Use for schemas, imports, query debugging, transactions, full-text search and Neo4j query adaptation, with local Python helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design and query LadybugDB graphs, adapt openCypher from Neo4j, and troubleshoot schema, import, transaction, and query behavior with local Python helpers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can query a local graph and can modify or create a database when write access is explicitly enabled.

Mitigation: Review the Cypher and database path, keep the default read-only mode, and enable writes only with authorization; use a recoverable copy and a transaction for write batches.

Risk: Cypher imports, procedures, and extensions may access local files or network resources, and the helper does not constrain host access.

Mitigation: Review COPY, LOAD, CALL, extensions, and paths; use trusted absolute import paths and review tool permissions in the execution environment.

## Reference(s):

- [Python and Cypher API reference](references/api-reference.md)
- [Ladybug workflow patterns](references/workflow-patterns.md)
- [LadybugDB Python API](https://docs.ladybugdb.com/client-apis/python/)
- [LadybugDB Cypher differences](https://docs.ladybugdb.com/cypher/difference/)
- [ClawHub skill release](https://clawhub.ai/ricardodpalmeida/skills/ladybug-opencypher-updated)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Cypher and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include query result previews, execution limits, and read-back checks.]

## Skill Version(s):

1.1.5 (source: changelog, released 2026-11-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
