## Description:

Guides developers working with Neon Postgres connections, migrations, branching, performance diagnostics, and Lakebase Search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure and troubleshoot existing Neon Postgres projects, manage schema changes and branches, and implement vector, full-text, or hybrid search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Database-changing steps, including migrations, extensions, indexes, and branch creation, can affect project data or availability.

Mitigation: Review changes before execution and test migrations on an isolated branch with a direct connection.

Risk: Updating .env can overwrite existing settings or expose database credentials.

Mitigation: Read the existing file first, preserve its settings, and keep credentials out of shared output.

Risk: English text-search configuration may produce poor search results for non-English corpora.

Mitigation: Select a PostgreSQL text-search configuration that matches the corpus.

Risk: Unpinned Drizzle tooling can make schema changes hard to reproduce.

Mitigation: Use pinned or project-local Drizzle tooling when generating and applying migrations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/andrelandgraf/skills/neon-postgres)
- [Neon connection methods](https://neon.com/docs/connect/choose-connection.md)
- [Neon connection pooling](https://neon.com/docs/connect/connection-pooling.md)
- [Neon database inspection](https://neon.com/docs/cli/inspect.md)
- [Lakebase Search getting started](https://neon.com/docs/ai/lakebase-search-get-started)
- [Vector search guide](artifact/references/vector-search.md)
- [Full-text search guide](artifact/references/full-text-search.md)
- [Hybrid search guide](artifact/references/hybrid-search.md)
- [Lakebase Search with Drizzle](artifact/references/lakebase-search-drizzle.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with SQL, TypeScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include database migrations and environment configuration.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
