## Description:

API自动生成工具 helps developers use magic-api to create HTTP interfaces from Web UI scripts, including database operations and business logic without hand-writing Controller, Service, or DAO layers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for magic-api projects when they need guidance, code snippets, and configuration for mapping scripts to HTTP interfaces and working with database-backed business logic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command authority for magic-api development workflows.

Mitigation: Use it only for explicit magic-api development work, avoid broad credentials, and require user confirmation before command execution or file writes.

Risk: Generated scripts or configuration may change databases or become reachable HTTP endpoints.

Mitigation: Review generated logic before deployment and require confirmation before database changes or publishing scripts as HTTP endpoints.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/magic-api-generate)
- [Publisher Profile](https://clawhub.ai/user/thcjp)
- [SkillHub Skill Homepage](https://skillhub.cn/skill/)
- [语法参考](/api/v1/skills/magic-api-generate/file?path=references%2Fsyntax.md&ownerHandle=webx32)
- [数据库操作](/api/v1/skills/magic-api-generate/file?path=references%2Fdatabase.md&ownerHandle=webx32)
- [业务示例](/api/v1/skills/magic-api-generate/file?path=references%2Fexamples.md&ownerHandle=webx32)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, shell command, configuration, and JSON-style result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated guidance may include database-facing or HTTP endpoint behavior that should be reviewed before use.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
