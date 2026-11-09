## Description:

Guides developers working with Neon Postgres on connections, schema changes, database branches, performance, and Lakebase Search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers managing an existing Neon Postgres database use this skill to choose connection methods, plan migrations and branches, troubleshoot performance and egress, and implement vector, full-text, or hybrid search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Schema migrations and branch operations can affect existing databases and workloads.

Mitigation: Test migrations on a production-like branch and verify branch protection and expiration settings before changing existing branches.

Risk: Connection strings and private document content may be exposed through local configuration or external embedding, reranking, and cache services.

Mitigation: Limit access to the intended project, protect connection strings in .env, and approve external services for the data before use.

Risk: The behavior of remotely fetched skills and external providers' data retention was not assessed.

Mitigation: Review remotely fetched skill content and confirm provider data handling before using sensitive material.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/andrelandgraf/skills/neon-postgres)
- [Parent Neon skill](https://neon.com/docs/ai/skills/neon/SKILL.md)
- [Branching workflows](artifact/references/branching.md)
- [Egress optimization](artifact/references/egress-optimization.md)
- [Vector search](artifact/references/vector-search.md)
- [Full-text search with BM25](artifact/references/full-text-search.md)
- [Hybrid search](artifact/references/hybrid-search.md)
- [Lakebase Search with Drizzle](artifact/references/lakebase-search-drizzle.md)
- [Neon connection methods](https://neon.com/docs/connect/choose-connection.md)
- [Neon database branching](https://neon.com/docs/introduction/branching.md)
- [Neon database inspection CLI](https://neon.com/docs/cli/inspect.md)
- [Lakebase Search guide](https://neon.com/docs/ai/lakebase-search-get-started)
- [Lakebase vector extension](https://neon.com/docs/extensions/lakebase-vector)
- [Lakebase text extension](https://neon.com/docs/extensions/lakebase-text)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with SQL, shell commands, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision guidance and examples; no fixed output schema]

## Skill Version(s):

1.0.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
