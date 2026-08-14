## Description:

Lifecycle guard for skill-augmented coding agents covering preflight and runtime phases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxf203](https://clawhub.ai/user/yxf203)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use SKILL Sonar to review candidate skills before installation and to route active skill use through advisory runtime guards for inputs, plans, tools, execution, memory, and outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add friction around tool calls, file writes, credentials, deletion, external network effects, and other high-impact actions.

Mitigation: Use the documented risk levels so low-risk reads stay silent while R2 and R3 actions receive targeted review or user confirmation.

Risk: The guard is advisory markdown, so its protections depend on the agent loading and following the relevant guard files.

Mitigation: Pair the skill with a host or review process that requires loading the preflight or runtime guard for the matching skill lifecycle step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yxf203/skills/skill-sonar)
- [Skill route](artifact/SKILL.md)
- [Preflight guard](artifact/preflight/preflight-guard.md)
- [Runtime guard](artifact/runtime/runtime-guard.md)
- [Runtime checklists](artifact/runtime/checklists/)
- [Runtime stage guards](artifact/runtime/stages/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with short guard-response lines and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory only; R0 actions remain silent and R1+ actions use a structured guard response.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
