## Description:

Designs and queries LadybugDB graphs with openCypher. Use for schemas, imports, query debugging, transactions, full-text search and Neo4j query adaptation, with local Python helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design and query LadybugDB graph databases, adapt openCypher queries, inspect schemas, and work through imports, transactions, and full-text search. It provides local Python helper guidance for safe query execution and runtime checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved writes or database creation can change graph data.

Mitigation: Use the owning application's access path, obtain write authorization, back up important data, and verify properties and relationship direction after changes.

Risk: Read-only database access does not sandbox host files or network resources; queries, import paths, and extensions can access them.

Mitigation: Review COPY, LOAD, CALL, paths, and extensions before execution; use trusted absolute import paths and install only authorized, compatible extensions.

Risk: Statements outside an explicit transaction may commit separately, leaving partial changes if a later statement fails.

Mitigation: Use an explicit transaction for atomic batches and inspect database state before retrying a failed batch.

## Reference(s):

- [LadybugDB API reference](artifact/references/api-reference.md)
- [Ladybug workflow patterns](artifact/references/workflow-patterns.md)
- [LadybugDB Python API](https://docs.ladybugdb.com/client-apis/python/)
- [LadybugDB migration guide](https://docs.ladybugdb.com/migrate/)
- [LadybugDB Cypher differences](https://docs.ladybugdb.com/cypher/difference/)
- [ClawHub release page](https://clawhub.ai/ricardodpalmeida/skills/ladybug-opencypher-updated)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with openCypher queries, Python examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and query bounds are tailored to the graph schema and task.]

## Skill Version(s):

1.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
