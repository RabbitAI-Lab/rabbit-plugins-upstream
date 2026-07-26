## Description: <br>
A comprehensive KingbaseES V8/V9 skill pack that helps agents answer questions and produce guidance for deployment, SQL, drivers, frameworks, operations, performance tuning, migration, troubleshooting, and extensions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wklxd](https://clawhub.ai/user/wklxd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DBAs, and operators use this skill pack to get KingbaseES V8/V9 guidance across installation, SQL usage, language drivers, framework integration, backup, high availability, security, monitoring, performance tuning, migration, troubleshooting, vector search, and MCP access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill pack persistently changes agent behavior and uses broad auto-triggers. <br>
Mitigation: Install it only for projects that actively use KingbaseES and review which skills are enabled before relying on automatic invocation. <br>
Risk: Guidance can include high-impact database or system commands. <br>
Mitigation: Review commands before execution, require backups and a rollback plan for production, and avoid DROP, TRUNCATE, trust authentication, or system-level changes unless explicitly approved. <br>
Risk: Examples may contain weak or sample credentials. <br>
Mitigation: Replace all sample passwords and secrets with approved credentials before use. <br>
Risk: Unrestricted MCP mode may allow read/write database access. <br>
Mitigation: Avoid unrestricted MCP mode unless it is required, and use least-privilege database accounts when enabling MCP tools. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wklxd/skills/kes-skills) <br>
- [Publisher Profile](https://clawhub.ai/user/wklxd) <br>
- [Artifact README](artifact/README.en.md) <br>
- [Top-Level Skill Manifest](artifact/SKILL.md) <br>
- [KingbaseES MCP Tools Reference](artifact/kes-mcp/ref/tools-reference.md) <br>
- [SQL Optimization Patterns](artifact/kes-sql-tuning/ref/sql-optimization-patterns.md) <br>
- [Migration Best Practice](artifact/kes-migration/ref/migration-best-practice.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include database and system commands that require review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
