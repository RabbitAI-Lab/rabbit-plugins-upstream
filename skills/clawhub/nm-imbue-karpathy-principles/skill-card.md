## Description: <br>
Pre-implementation gate covering think-first, simplicity, surgical edits, and verifiable goals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill as a pre-flight and self-review gate for non-trivial coding work, especially when a task needs assumptions surfaced, scope constrained, changes kept surgical, and success criteria made verifiable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can slow down trivial fixes, exploratory spikes, documentation-only changes, time-boxed prototypes, or production-fire response. <br>
Mitigation: Apply the documented tradeoff guidance and skip or lighten the gate when the cost of extra deliberation is higher than the risk of a wrong-shaped change. <br>
Risk: Generic triggers may invoke the skill more often than intended. <br>
Mitigation: Review the trigger set during installation and narrow triggers if the gate interrupts normal workflow. <br>
Risk: The skill's recommendations can shape code changes even though they are guidance rather than guarantees. <br>
Mitigation: Review proposed assumptions, scope choices, diffs, and verification steps before relying on them for production work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-karpathy-principles) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown guidance with checklists, review questions, and worked examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no hidden execution, data access, or persistence was identified in the server security evidence.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
