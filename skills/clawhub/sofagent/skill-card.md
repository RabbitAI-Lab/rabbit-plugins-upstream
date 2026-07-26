## Description: <br>
Sofagent adds an agent governance and reflection layer for keeping work scoped, checking risky actions, recording task outcomes, and preserving lessons across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongfangxun](https://clawhub.ai/user/kongfangxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add task gates, scope checks, reflection, and closure routines to agent sessions that involve complex work, multi-file changes, or higher-risk operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill changes agent behavior across a session and may influence task acceptance, execution, and closure decisions. <br>
Mitigation: Review the injected guidance before deployment and confirm that its gates, escalation behavior, and completion criteria match the intended operating policy. <br>
Risk: The skill may read and write persistent .sofagent memory, task logs, evaluation records, orchestration records, and knowledge files. <br>
Mitigation: Set retention and sanitization controls before use on sensitive projects, and periodically review stored records for unnecessary or sensitive data. <br>
Risk: The security scan notes under-scoped external and local tooling behavior. <br>
Mitigation: Review configured scripts and disable or pin live GitHub or template lookup when supply-chain control is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/kongfangxun) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline bash or PowerShell commands and local file-record templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update .sofagent memory, task logs, evaluation records, orchestration records, and knowledge files.] <br>

## Skill Version(s): <br>
1.1.9 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
