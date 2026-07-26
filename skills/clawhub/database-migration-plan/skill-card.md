## Description: <br>
Write a safe, zero-downtime database migration plan for a schema change, including migration objectives, backward compatibility analysis, expand/contract phases, SQL, rollback steps, validation queries, and a deployment runbook. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, database engineers, and technical leads use this skill to plan schema changes that preserve availability, data consistency, and rollback options across staged deployments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated migration plans may include destructive contract steps, such as dropping columns, that can cause data loss if run without review. <br>
Mitigation: Review the plan with a DBA or technical lead before production use, and verify rollback windows, validation queries, and destructive steps before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/database-migration-plan) <br>
- [Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/database-migration-plan.html) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with SQL, checklist, and runbook sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces planning guidance only; it does not execute commands or access systems.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
