## Description: <br>
Guides agents on when to ask clarifying questions versus proceed autonomously when user intent is clear. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to reduce unnecessary clarification loops while preserving explicit confirmation for ambiguous, destructive, security-sensitive, production, migration, or externally visible work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The autonomy guidance could be over-applied to destructive, security-sensitive, production, data migration, or externally visible tasks. <br>
Mitigation: Require explicit confirmation for those task classes even when the skill encourages proceeding with ordinary reversible work. <br>
Risk: An agent may proceed when ambiguity materially affects correctness. <br>
Mitigation: Use the skill's ask thresholds, previews, dry runs, small reviewable changes, and rollback planning before finalizing work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-decisive-action) <br>
- [Project homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown] <br>
**Output Format:** [Markdown guidance with examples and decision checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable output; intended to shape agent decision-making behavior.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
