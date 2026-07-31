## Description: <br>
Assesses architecture decisions, ADR compliance, and coupling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review architecture changes, ADR compliance, module coupling, design invariants, and architecture risks before merging significant system changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad architecture or design wording. <br>
Mitigation: Invoke it intentionally for architecture review rather than general design discussion. <br>
Risk: Architecture recommendations can be incorrect or misleading if repository context is incomplete. <br>
Mitigation: Require evidence-backed findings with file paths, line references, and human review before acting on recommendations. <br>
Risk: The skill includes repository-inspection shell commands. <br>
Mitigation: Review commands before execution and keep them scoped to the target repository. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-architecture-review) <br>
- [Declared homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [FPF Framework](https://github.com/ailev/FPF) <br>
- [quint-code](https://github.com/m0n0x41d/quint-code) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with checklists, review sections, command snippets, findings, and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for human review and may include approve, approve-with-actions, or block recommendations.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
