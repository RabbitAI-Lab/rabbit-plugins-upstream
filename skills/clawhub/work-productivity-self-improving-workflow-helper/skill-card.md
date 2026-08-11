## Description:

Helps AI-agent users, skill authors, maintainers, and teams turn self-improving and proactive-agent workflow needs into practical artifacts, checklists, analysis, code changes, or decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to clarify productivity or self-improvement workflow requests, produce an actionable artifact, and check the result against success criteria. It is especially suited for bug-fix planning, setup hardening, reliability improvement, reusable checklists, and adjacent skill design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may cause the skill to be selected for ordinary bug-fix, learning, organizing, or self-improvement requests where a narrower skill would be more appropriate.

Mitigation: Tighten or disable implicit activation when broad productivity workflow help is not desired.

Risk: Workflow recommendations, code changes, or checklists may be incomplete or misleading if the user's constraints and success criteria are underspecified.

Mitigation: Restate the outcome, constraints, available inputs, and success criteria before producing the final artifact, then include a verification note.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Release Page](https://clawhub.ai/kyro-ma/skills/work-productivity-self-improving-workflow-helper)
- [Self-improving Agent Demand Signal](https://clawhub.ai/skills/self-improving-agent)
- [Proactive Agent Demand Signal](https://clawhub.ai/skills/proactive-agent)
- [Self-Improving + Proactive Agent Demand Signal](https://clawhub.ai/skills/self-improving)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown text with optional code, shell-command, checklist, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, limits, validation notes, and follow-up work when useful.]

## Skill Version(s):

0.20260811.40534 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
