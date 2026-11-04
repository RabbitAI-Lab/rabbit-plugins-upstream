## Description:

Neon Realtime makes any SQL query live. Build realtime, reactive apps and agents on Lakebase Postgres with live SQL queries and reactivity primitives. Use when app UI or agent state must update live from database rows (dashboards, feeds, collaboration, multi-user or multi-device sync), for optimistic mutations, or to replace polling or other realtime sync systems. Triggers include "live query", "subscribe", "sync engine", "useLiveQuery", "TanStack DB", "optimistic updates", "@neon/realtime". For push that doesn't come from database rows (presence, typing, LLM streams), use neon-functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build apps and agents that subscribe to live, authorized Postgres query results, apply optimistic writes, and keep client state synchronized without polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live query may expose rows if it is sealed without checking the caller and restricting the query to authorized data.

Mitigation: Authenticate before sealing, scope each query to authorized rows, validate client-supplied parameters, and recheck the session on renewals and writes; Realtime does not enforce RLS.

Risk: Exposing database or signing secrets can allow unauthorized access or query sealing.

Mitigation: Keep database and signing secrets server-side, restrict allowed origins, and rotate exposed secrets.

## Reference(s):

- [Queries](artifact/references/queries.md)
- [Client-side reactivity](artifact/references/reactivity.md)
- [Optimistic mutations](artifact/references/mutations.md)
- [Subscribing](artifact/references/subscribing.md)
- [Server-side rendering](artifact/references/ssr.md)
- [Neon Realtime overview](https://neon.com/docs/realtime/overview.md)
- [Neon Realtime quickstart](https://neon.com/docs/realtime/quickstart.md)
- [Neon Realtime TypeScript SDK reference](https://neon.com/docs/realtime/sdks/typescript.md)
- [Neon Realtime CLI](https://neon.com/docs/cli/realtime.md)
- [Neon parent skill](https://neon.com/docs/ai/skills/neon/SKILL.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with TypeScript, SQL, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
