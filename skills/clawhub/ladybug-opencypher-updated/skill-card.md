## Description:

Designs and queries LadybugDB graphs with openCypher. Use for schemas, imports, query debugging, transactions, full-text search and Neo4j query adaptation, with local Python helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and graph engineers use this skill to design LadybugDB schemas, import and query graph data, debug Cypher, adapt Neo4j queries, and make authorized database changes with read-back checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read-only database mode does not restrict host file or network access from queries.

Mitigation: Review file paths, COPY, LOAD, CALL, and extensions; use trusted absolute import paths and select the intended database.

Risk: Authorized writes can change graph data, and separately committed statements may leave partial changes after a failure.

Mitigation: Confirm authorization, use backups and explicit transactions for write batches, then read back the affected properties and relationships.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ricardodpalmeida/skills/ladybug-opencypher-updated)
- [LadybugDB API reference](references/api-reference.md)
- [Workflow patterns](references/workflow-patterns.md)
- [LadybugDB Python API documentation](https://docs.ladybugdb.com/client-apis/python/)
- [LadybugDB installation guide](https://docs.ladybugdb.com/installation/)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with openCypher and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded query previews, execution counts, and read-back checks.]

## Skill Version(s):

1.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
