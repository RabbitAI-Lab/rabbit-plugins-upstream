## Description: <br>
通过 Admin API 或 CLI 管理 Node-RED 实例，支持可回滚的流程部署、多实例管理、节点依赖治理、Context 持久化和安全加固。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, automation engineers, and operations teams use this skill to administer Node-RED instances, version and deploy flows, manage nodes, back up or restore state, and apply operational safety checks across development, staging, and production environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide production-impacting Node-RED deploy, delete, restore, rollback, upgrade, and Docker operations. <br>
Mitigation: Require explicit human confirmation before production operations and prefer staging validation before deploying to production. <br>
Risk: Weak scoping could let an agent administer unintended Node-RED instances. <br>
Mitigation: Configure only intended instances, use least-privilege credentials, and keep development or staging as the default target. <br>
Risk: Backups may contain credentials or other sensitive operational state. <br>
Mitigation: Store backups in encrypted storage and avoid committing backup files to public repositories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/flow-editor-pro) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, configuration snippets, operational checklists, and troubleshooting tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose production-impacting Node-RED Admin API, CLI, rollback, restore, upgrade, and Docker operations that require human review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
