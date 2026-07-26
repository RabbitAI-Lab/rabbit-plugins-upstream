## Description: <br>
Designs Prisma schemas, writes type-safe queries, and fixes migrations, connection pools, and N+1 relation loads in Node and TypeScript. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design Prisma schemas, plan migrations, write Prisma Client queries, debug Prisma error codes, and handle deployment, testing, connection pooling, TypeScript, and raw SQL escape-hatch workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store Prisma-specific preferences and memory under ~/Clawic/data/prisma. <br>
Mitigation: Install only if local preference storage at that path is acceptable, and review stored configuration when troubleshooting repeated guidance. <br>
Risk: Generated migration, raw SQL, db push, migrate reset, or force-reset commands can affect schema or data. <br>
Mitigation: Review proposed commands and SQL before execution, especially destructive or production-facing migration steps. <br>
Risk: Test reset guidance can damage non-test data if pointed at the wrong database. <br>
Mitigation: Confirm reset commands target an isolated test database before running them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/prisma) <br>
- [Skill Homepage](https://clawic.com/skills/prisma) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline Prisma schema, TypeScript, SQL, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose edits, commands, migration plans, configuration values, and review checklists for Prisma projects.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
