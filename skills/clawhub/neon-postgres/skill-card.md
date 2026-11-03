## Description:

Guides developers working with existing Neon Postgres databases on connections, migrations, branching, performance, egress, and semantic, full-text, and hybrid search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to configure connections, plan and test schema changes, manage Neon branches, diagnose performance and egress issues, and implement search workflows for an existing Postgres database.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text and cached rows may be processed by the selected cloud services.

Mitigation: Confirm that the selected services’ data handling meets the project’s privacy requirements.

Risk: Branch protections and expiry settings may differ from assumptions.

Mitigation: Verify the actual protection and expiry settings after deployment.

Risk: A migration could affect production data if it targets the wrong project or branch.

Mitigation: Confirm the intended project and branch, and test migrations away from production.

## Reference(s):

- [Neon branching guide](https://neon.com/docs/introduction/branching.md)
- [Branching workflows](references/branching.md)
- [Egress optimization](references/egress-optimization.md)
- [Neon CLI database inspection](https://neon.com/docs/cli/inspect.md)
- [Neon query performance](https://neon.com/docs/postgresql/query-performance.md)
- [Neon autoscaling](https://neon.com/docs/introduction/autoscaling.md)
- [Neon scale to zero](https://neon.com/docs/introduction/scale-to-zero.md)
- [Neon instant restore](https://neon.com/docs/introduction/branch-restore.md)
- [Neon connection pooling](https://neon.com/docs/connect/connection-pooling.md)
- [Neon IP allow lists](https://neon.com/docs/introduction/ip-allow.md)
- [Neon logical replication](https://neon.com/docs/guides/logical-replication-guide.md)
- [Lakebase Search getting started](https://neon.com/docs/ai/lakebase-search-get-started)
- [Vector search](references/vector-search.md)
- [Full-text search](references/full-text-search.md)
- [Hybrid search](references/hybrid-search.md)
- [Lakebase Search with Drizzle](references/lakebase-search-drizzle.md)

## Skill Output:

**Output Type(s):** [Guidance, SQL, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with SQL, shell, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and examples are tailored to the existing database, project, branch, application stack, and stated task.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
