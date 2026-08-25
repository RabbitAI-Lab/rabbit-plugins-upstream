## Description:

Helps AI-agent users, skill authors, maintainers, and teams turn proactive productivity workflow requests into practical plans, artifacts, checklists, analysis, code changes, or decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to adapt proven proactive-agent workflow patterns into reliable local workflows. It helps clarify outcomes and constraints, produce a concrete deliverable, and verify the result against the user's success criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad auto-invocation wording may route general productivity or bug-fix requests to this skill too readily.

Mitigation: Review trigger terms before deployment and narrow them if precise routing matters in a multi-skill environment.

Risk: Generated plans, checklists, code changes, or guidance may be incomplete or mismatched to the user's actual constraints.

Mitigation: Require visible assumptions, success criteria, validation notes, and remaining risks in the final output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-proactive-agent-workflow-helper)
- [Requirement plan](references/requirement-plan.md)
- [Popular ClawHub skill demand: Proactive Agent](https://clawhub.ai/skills/proactive-agent)
- [Popular ClawHub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving)
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology)
- [Skills weekly issue, 2026-08-17](https://github.com/shufanli/AI-Product-Compass/issues/48)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional code, shell command, checklist, and configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include visible assumptions, limits, validation notes, and follow-up work when helpful.]

## Skill Version(s):

0.20260825.44155 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
