## Description:

Provides guidance for connecting to and managing Neon-hosted Lakebase Postgres databases, including schema changes, branching, performance, egress, and full-text, vector, and hybrid search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to work with existing Neon Postgres projects, connections, schemas, and branches. It also guides database diagnostics and the implementation of Lakebase full-text, vector, and hybrid search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Database changes or branch operations could affect production data.

Mitigation: Use credentials scoped to the intended project and test changes on a development branch.

Risk: Embedding, reranking, or external caching services may process document text and database fields.

Mitigation: Confirm the selected services are approved to process the data involved before enabling them.

Risk: The separately fetched parent skill and external dependencies were outside this artifact review.

Mitigation: Review the parent skill and use locked dependency versions before relying on their guidance.

## Reference(s):

- [Branching workflows](artifact/references/branching.md)
- [Egress optimization](artifact/references/egress-optimization.md)
- [Full-text search](artifact/references/full-text-search.md)
- [Hybrid search](artifact/references/hybrid-search.md)
- [Lakebase Search with Drizzle](artifact/references/lakebase-search-drizzle.md)
- [Semantic vector search](artifact/references/vector-search.md)
- [Neon connection methods](https://neon.com/docs/connect/choose-connection.md)
- [Neon database branching](https://neon.com/docs/introduction/branching.md)
- [Neon database inspection](https://neon.com/docs/cli/inspect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with SQL, TypeScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
