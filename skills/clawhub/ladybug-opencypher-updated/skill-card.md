## Description:

Guides developers in designing and querying local LadybugDB graphs with openCypher, including schema design, imports, transactions, search, and query troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design local property graphs, adapt and troubleshoot openCypher queries, and run reviewed queries against LadybugDB databases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries can access local database files and may change data when write access is enabled.

Mitigation: Confirm the target database and query scope; require explicit approval before using --write or --create on an important database.

Risk: Cypher operations such as COPY, LOAD, CALL, and extension use may access additional files or resources even when the database is opened read-only.

Mitigation: Review Cypher statements, extension use, and file paths before execution; use trusted paths and the application's existing database access route.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ricardodpalmeida/skills/ladybug-opencypher-updated)
- [LadybugDB Python and Cypher API reference](artifact/references/api-reference.md)
- [LadybugDB workflow patterns](artifact/references/workflow-patterns.md)
- [LadybugDB Python API](https://docs.ladybugdb.com/client-apis/python/)
- [LadybugDB concurrency](https://docs.ladybugdb.com/concurrency/)
- [LadybugDB Neo4j differences](https://docs.ladybugdb.com/cypher/difference/)

## Skill Output:

**Output Type(s):** [Guidance, Cypher queries, Shell commands, Code]

**Output Format:** [Markdown guidance with Cypher, Python, and shell examples; text query-result previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local query helper is read-only by default; writes and database creation require explicit flags.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
