## Description: <br>
Guides agents through Neon Lakebase Postgres setup, connection methods, drivers, branching, autoscaling, scale-to-zero, instant restore, read replicas, connection pooling, IP allow lists, and logical replication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrelandgraf](https://clawhub.ai/user/andrelandgraf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to choose safe Neon Postgres setup, connection, schema, branching, scaling, restore, replica, pooling, allow-list, and replication workflows for application projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may target the wrong Neon organization, project, branch, or connection type. <br>
Mitigation: Confirm the intended organization, project, branch, and pooled or direct connection path before applying setup or connection guidance. <br>
Risk: DATABASE_URL is a credential-bearing setting and may be changed during environment setup. <br>
Mitigation: Review existing .env contents and any proposed DATABASE_URL changes before writing or sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andrelandgraf/skills/neon-postgres) <br>
- [Neon parent skill](https://neon.com/docs/ai/skills/neon/SKILL.md) <br>
- [Choose a connection method](https://neon.com/docs/connect/choose-connection.md) <br>
- [Drizzle and Neon](https://neon.com/docs/guides/drizzle.md) <br>
- [Neon serverless driver](https://neon.com/docs/serverless/serverless-driver.md) <br>
- [Neon branching](https://neon.com/docs/introduction/branching.md) <br>
- [Neon Postgres branches skill](https://neon.com/docs/ai/skills/neon-postgres-branches/SKILL.md) <br>
- [Neon autoscaling](https://neon.com/docs/introduction/autoscaling.md) <br>
- [Neon scale to zero](https://neon.com/docs/introduction/scale-to-zero.md) <br>
- [Neon instant restore](https://neon.com/docs/introduction/branch-restore.md) <br>
- [Neon read replicas](https://neon.com/docs/introduction/read-replicas.md) <br>
- [Neon connection pooling](https://neon.com/docs/connect/connection-pooling.md) <br>
- [Neon IP allow lists](https://neon.com/docs/introduction/ip-allow.md) <br>
- [Neon logical replication](https://neon.com/docs/guides/logical-replication-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Neon CLI, MCP, driver, ORM, DATABASE_URL, and connection-type choices for the user's project.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
