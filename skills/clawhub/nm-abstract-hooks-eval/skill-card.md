## Description: <br>
Evaluate hook security, performance, and SDK compliance for Claude/OpenClaw hook audits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent-tooling reviewers use this skill to audit Claude/OpenClaw hooks for security, performance, compliance, reliability, and maintainability before adopting or deploying hook behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example hook guidance may be adapted into real hooks that observe or influence agent actions. <br>
Mitigation: Review and scan any implemented hook code separately before deployment. <br>
Risk: Broad trigger words may activate the skill during generic security or performance discussions. <br>
Mitigation: Use the guidance in contexts where hook auditing is relevant and confirm applicability before acting on recommendations. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [SDK Hook Types](modules/sdk-hook-types.md) <br>
- [Hook Evaluation Criteria](modules/evaluation-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with command examples and scoring criteria] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no installed executable behavior.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
