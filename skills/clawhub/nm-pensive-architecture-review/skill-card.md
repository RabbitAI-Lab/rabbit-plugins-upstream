## Description: <br>
Assesses architecture decisions, ADR compliance, and coupling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review architecture changes before merge, including ADR compliance, module coupling, design invariants, security and performance checks, and follow-up actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may cause the skill to activate during general design or pattern discussions. <br>
Mitigation: Narrow the trigger wording or invoke the skill explicitly when architecture review is intended. <br>
Risk: Architecture recommendations can be incorrect if the agent silently revises existing design invariants. <br>
Mitigation: Use the skill's invariant-conflict workflow to present preserve, layer, and revise options and escalate the final decision to a human reviewer. <br>


## Reference(s): <br>
- [Pensive plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [ADR Audit Module](modules/adr-audit.md) <br>
- [Coupling Analysis Module](modules/coupling-analysis.md) <br>
- [Principle Checks Module](modules/principle-checks.md) <br>
- [FPF Architecture Review Methodology](modules/fpf-methodology.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, checklists, diagrams, findings, recommendations, and follow-up actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include approve, approve-with-actions, or block recommendations for architecture reviews.] <br>

## Skill Version(s): <br>
1.9.16 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
