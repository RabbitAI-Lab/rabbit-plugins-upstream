## Description: <br>
Attack a risky design with a multi-agent workflow before writing code, using specialist review agents to find concrete failure scenarios and fixes across hardware, concurrency, security, data-format, crash-consistency, protocol, and CI-test-integrity concerns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickflach](https://clawhub.ai/user/nickflach) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill before implementing hard-to-debug or hard-to-reverse systems designs, such as device drivers, protocols, on-disk formats, concurrency paths, capability checks, and CI gates. It helps them run a focused adversarial design review, reconcile findings, and turn validated claims into runtime tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Specialist review agents may read project files named in the design brief. <br>
Mitigation: Use the skill only in workspaces where that code access is appropriate and keep the design brief limited to files needed for the review. <br>
Risk: Adversarial findings can be overstated or based on an incomplete reading of the real code. <br>
Mitigation: Reconcile each finding against the actual project context, apply confirmed blockers or major issues, and discard refuted findings with a reason. <br>
Risk: A proposed design fix may still be unproven after implementation. <br>
Mitigation: Gate each accepted claim with a runtime signal such as a boot-log line, captured packet, disk readback, or denied capless-caller test. <br>


## Reference(s): <br>
- [Adversarial Design Review Field Playbook](docs/PLAYBOOK.md) <br>
- [Attack Workflow Template](resources/attack-workflow.template.js) <br>
- [QuantumOS example project](https://github.com/flaukowski/QuantumOS) <br>
- [ClawHub skill page](https://clawhub.ai/nickflach/skills/adversarial-design-review) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown guidance with a JavaScript workflow template and structured findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces design critique, ranked findings, concrete fixes, and reconciliation guidance; review agents may read project files named in the design brief.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, created 2026-07-15) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
