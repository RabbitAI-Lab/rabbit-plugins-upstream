## Description: <br>
GraphQL helps developers design, debug, and harden GraphQL schemas, resolvers, clients, subscriptions, federation, caching, and production operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when designing or reviewing GraphQL schemas, SDL, resolvers, mutations, pagination, authorization, caching, subscriptions, federation, and production hardening. It also supports diagnosis of GraphQL-specific failures such as N+1 query storms, null propagation, partial responses with errors, stale client caches, and breaking schema changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GraphQL debugging output, logs, and command examples can expose tokens, cookies, passwords, personal data, or tenant-specific records. <br>
Mitigation: Redact sensitive values before sharing or storing logs, and prefer logging operation names, request IDs, and variable keys rather than raw variables. <br>
Risk: The skill may store GraphQL preferences and project context in ~/Clawic/data/graphql/. <br>
Mitigation: Treat the local configuration and memory files as project context, avoid storing secrets there, and review them before export or sharing. <br>


## Reference(s): <br>
- [ClawHub GraphQL skill page](https://clawhub.ai/ivangdavila/skills/graphql) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic GraphQL skill page](https://clawic.com/skills/graphql) <br>
- [GraphQL skill overview](artifact/SKILL.md) <br>
- [Security guidance](artifact/security.md) <br>
- [Setup and local preference storage](artifact/setup.md) <br>
- [Command examples](artifact/commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with GraphQL, JSON, YAML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local preferences from ~/Clawic/data/graphql/ and may advise writing configuration or memory there when the user states a preference.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
