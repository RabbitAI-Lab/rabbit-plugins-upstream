## Description: <br>
Guides when to ask clarifying questions versus proceed autonomously to reduce unnecessary clarifying questions when intent is clear. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to decide when to ask clarifying questions and when to proceed with a standard, reversible implementation. It is intended to reduce unnecessary interruptions while preserving explicit confirmation for destructive, security-critical, migration, deployment, or otherwise high-impact work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may make an agent more proactive and reduce clarifying questions. <br>
Mitigation: Require explicit approval before the agent changes external systems, deletes data, deploys code, handles credentials, or makes security-sensitive changes. <br>
Risk: Proceeding autonomously on ambiguous or high-impact requests can produce incorrect or unsafe changes. <br>
Mitigation: Use dry runs, previews, backups, incremental changes, and explicit confirmation for destructive, security-critical, migration, breaking-change, or production deployment work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-decisive-action) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown guidance with decision tables, checklists, examples, and concise response patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No API keys, MCP tools, or credential environment variables were detected.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
