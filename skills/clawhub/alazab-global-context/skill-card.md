## Description: <br>
Shared production context, operational paths, orchestration policies, agent routing, approvals, deployment and execution standards for all Alazab Portal AI agents, models, sessions and nodes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alazabdev](https://clawhub.ai/user/alazabdev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to apply Alazab Portal AI production context across agents, sessions, nodes, and deployment workflows. It guides mission planning, agent routing, production execution, approvals, rollback, logging, and secret-handling standards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Global auto-attach behavior may cause this Alazab-specific production policy to influence every matching agent and session. <br>
Mitigation: Install only in the intended Alazab environment or narrow the attachment scope before use elsewhere. <br>
Risk: The skill contains production endpoints, paths, shell executor assumptions, and operational rules that may be unsafe if applied to a different infrastructure. <br>
Mitigation: Review and confirm the target nodes, paths, endpoints, and executor model before enabling the context. <br>
Risk: Some non-destructive production actions may proceed automatically under the disclosed approval policy. <br>
Mitigation: Keep approval gates enabled, require owner approval for destructive or irreversible operations, and audit command execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alazabdev/skills/alazab-global-context) <br>
- [Publisher profile](https://clawhub.ai/user/alazabdev) <br>
- [ClawHub homepage metadata](https://clawhub.ai/alazabdev) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration instructions, Markdown, Code, Shell commands] <br>
**Output Format:** [Markdown guidance and structured configuration context] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Applies globally through auto-attach behavior and may influence all matching agent sessions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
