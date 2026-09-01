## Description:

Cross-shift continuity and unresolved issue tracking system for restaurant and franchise operators. Captures wins, bottlenecks, and handoffs at end of shift, then actively tracks unresolved urgent items across shifts until they are confirmed closed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mcphersonai](https://clawhub.ai/user/mcphersonai)

### License/Terms of Use:

Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

## Use Case:

Restaurant and franchise operators use this skill to capture end-of-shift reflections, create structured urgent handoffs, and keep unresolved operational issues visible across shift changes until they are closed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shift reflections and unresolved operational issues may be persisted in the companion store memory system.

Mitigation: Confirm the store memory retention, deletion, access control, and audit policies before deployment; use operational roles instead of names and omit unnecessary PII.

Risk: One artifact line says unresolved issue tracking runs continuously in the background, which conflicts with the stated operator-triggered behavior.

Mitigation: Treat follow-up and issue tracking as operator-triggered until the publisher corrects the wording.

## Reference(s):

- [QSR Shift Reflection on ClawHub](https://clawhub.ai/mcphersonai/skills/qsr-shift-reflection)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text for shift reflections, open issues, issue boards, exports, and weekly digests.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are store-scoped when the companion memory skill is available and session-only otherwise.]

## Skill Version(s):

2.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
