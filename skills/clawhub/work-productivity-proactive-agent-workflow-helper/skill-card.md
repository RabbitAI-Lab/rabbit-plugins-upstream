## Description:

Helps AI-agent users, skill authors, maintainers, and teams turn proactive-agent workflow demand into practical plans, checklists, implementation support, and verification notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn proactive-agent and work-productivity requests into local-friendly workflows, artifacts, checklists, analyses, code changes, or decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may cause the skill to activate on general productivity or bug-fix prompts.

Mitigation: Narrow or disable implicit invocation in the agent runtime when the skill should only be used explicitly.

Risk: Workflow guidance can be incomplete or unsuitable if the user's goals, constraints, or success criteria are underspecified.

Mitigation: Restate assumptions and validate the produced artifact against the stated success criteria before applying it.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-proactive-agent-workflow-helper)
- [Popular ClawHub skill demand: Proactive Agent](https://clawhub.ai/skills/proactive-agent)
- [Popular ClawHub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving)
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text, with code blocks or shell commands when the user's task requires them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a short verification note, assumptions, limits, and follow-up risks.]

## Skill Version(s):

0.20260814.40500 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
