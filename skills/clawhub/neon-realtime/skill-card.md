## Description:

Guides developers in building reactive applications and agents with live SQL queries, subscriptions, and optimistic updates on Neon Realtime.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to implement live database-backed views and agent state, including subscriptions, authenticated queries, optimistic mutations, and server-side rendering.

### Deployment Geography for Use:

Global (Neon Realtime service availability varies by region)

## Known Risks and Mitigations:

Risk: Database credentials, Realtime secrets, and sealed queries could be exposed to clients, logs, URLs, or shared caches.

Mitigation: Keep secrets on the server; avoid logging or persisting sealed queries and review browser bundles and cache policies.

Risk: Live subscriptions or writes could expose or modify another user's data if authorization or session changes are mishandled.

Mitigation: Authenticate before sealing and writing, constrain queries to the authorized user, and discard subscriptions and cached rows when sessions change.

## Reference(s):

- [Neon Realtime ClawHub release](https://clawhub.ai/andrelandgraf/skills/neon-realtime)
- [Neon Realtime overview and regional availability](https://neon.com/docs/realtime/overview.md)
- [Neon Realtime quickstart](https://neon.com/docs/realtime/quickstart.md)
- [Neon Realtime TypeScript SDK reference](https://neon.com/docs/realtime/sdks/typescript.md)
- [Defining and authorizing live queries](https://neon.com/docs/realtime/guides/queries.md)
- [Optimistic mutations](https://neon.com/docs/realtime/guides/mutations.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with TypeScript and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples require adaptation to the application's database schema and authentication.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
