## Description: <br>
Evaluate hook security, performance, and SDK compliance. Use for audits <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit Claude Code hooks for security, performance, SDK compliance, reliability, and maintainability. It provides hook references, scoring criteria, quality gates, and example command workflows for reviewing hook implementations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms may surface this reference skill during general security or performance discussions. <br>
Mitigation: Confirm the task is specifically about hook evaluation before applying the guidance. <br>
Risk: Hook examples or audit workflows could lead users to log sensitive prompts, paths, commands, or tool results. <br>
Mitigation: Require disclosure and redaction for any hook logging or reporting that captures user, project, command, or tool-result data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-abstract-hooks-eval) <br>
- [OpenClaw Metadata Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Hook Evaluation Criteria](modules/evaluation-criteria.md) <br>
- [Python SDK Hook Types](modules/sdk-hook-types.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with command examples and scoring rubrics] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no active code or hidden execution.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
