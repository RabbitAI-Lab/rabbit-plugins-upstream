## Description: <br>
Pre-implementation gate covering think-first, simplicity, surgical edits, and verifiable goals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill as a pre-implementation and review gate for non-trivial coding tasks. It prompts assumption checks, scope control, surgical diffs, and verifiable success criteria before and after implementation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may slow or over-constrain trivial coding tasks because some triggers are broad. <br>
Mitigation: Apply the tradeoff guidance and keep the gate lightweight for obvious typo fixes, throwaway spikes, documentation-only edits, time-boxed prototypes, and urgent production fixes. <br>
Risk: Companion Night Market or Claude Code plugin components may introduce behavior outside this skill's markdown guidance. <br>
Mitigation: Review and scan any companion plugin agents, hooks, or commands before enabling them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-imbue-karpathy-principles) <br>
- [Claude Night Market imbue plugin](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code] <br>
**Output Format:** [Markdown guidance with checklists, scope rationale, and verification criteria] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, tradeoff notes, diff-trace checks, and test or command suggestions for verification.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
