## Description: <br>
Masterplan Executor helps an agent implement an existing project masterplan phase by phase, with research for ambiguity, production-readiness checks, self-audits, and a persistent execution log. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to start or continue implementation from an approved masterplan, keeping work aligned to the roadmap, acceptance criteria, tests, audits, and execution log. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make broad codebase changes and commits while executing a masterplan. <br>
Mitigation: Review the masterplan scope before use, run in version control, inspect diffs at each phase boundary, and require confirmation before commits when appropriate. <br>
Risk: The skill may use external web research automatically to resolve ambiguous or outdated implementation details. <br>
Mitigation: For private or regulated projects, require local-only operation or explicit approval before web access, and avoid exposing secrets, internal URLs, customer data, or proprietary details in searches or logs. <br>
Risk: The execution log can capture sensitive project details if used carelessly. <br>
Mitigation: Keep secrets, credentials, customer data, internal URLs, and proprietary implementation details out of docs/masterplan/execution-log.md. <br>


## Reference(s): <br>
- [Execution Standards](artifact/references/execution-standards.md) <br>
- [Phase Execution Checklist](artifact/references/phase-execution-checklist.md) <br>
- [Progress Log Template](artifact/references/progress-log-template.md) <br>
- [Resource-Safe Subagent Execution](artifact/references/resource-safety.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/anjasta-tarigan/skills/masterplan-executor) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with code, shell commands, and file changes as needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces phased implementation work and execution-log updates based on an existing masterplan.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
