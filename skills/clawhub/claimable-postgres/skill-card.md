## Description: <br>
Provision instant temporary Postgres databases via Claimable Postgres by Neon (neon.new) with no login, signup, or credit card. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrelandgraf](https://clawhub.ai/user/andrelandgraf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to provision short-lived Postgres databases for local development, demos, prototypes, and tests, then capture DATABASE_URL-style connection strings and claim links for project setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Temporary database credentials can be written into local env files. <br>
Mitigation: Confirm the target env file and variable key, avoid overwriting existing values, and ensure env files are ignored by version control. <br>
Risk: The skill can create external temporary Postgres databases for an agent workflow. <br>
Mitigation: Use it for development or test work, recommend standard Neon provisioning for production workloads, and provide the claim URL when persistence is needed. <br>
Risk: Seed SQL may be destructive if it contains DROP, TRUNCATE, or broad DELETE statements. <br>
Mitigation: Ask for confirmation before running destructive seed SQL and report what was executed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andrelandgraf/skills/claimable-postgres) <br>
- [Parent Neon skill](https://neon.com/docs/ai/skills/neon/SKILL.md) <br>
- [Claimable Postgres API base](https://neon.new/api/v1) <br>
- [Claimable Postgres docs](https://neon.com/docs/reference/claimable-postgres#vite-plugin) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline bash, JSON, and TypeScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to create temporary external Postgres databases and write DATABASE_URL values to env files.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
