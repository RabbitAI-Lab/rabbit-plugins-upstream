## Description:

Helps AI-agent users and skill authors turn demand for Proactive Agent-style workflows into practical plans, checklists, analyses, code changes, or implementation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and teams use this skill to structure proactive-agent workflow requests into concrete artifacts such as plans, checklists, analyses, code changes, or decision support. It is intended for productivity and reliability work around agent workflows that should remain feasible on ordinary local hardware.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic invocation wording may cause the skill to appear for ordinary productivity or task requests.

Mitigation: Review and narrow activation triggers or platform invocation settings before deployment where unwanted invocation would disrupt workflows.

Risk: Generated workflow, checklist, analysis, or code guidance may be incomplete or misleading if the user's context is underspecified.

Mitigation: Require visible assumptions, success criteria, validation notes, and remaining risks in outputs before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-proactive-agent-workflow-helper)
- [Requirement Plan](references/requirement-plan.md)
- [Proactive Agent demand signal](https://clawhub.ai/skills/proactive-agent)
- [Self-Improving + Proactive Agent demand signal](https://clawhub.ai/skills/self-improving)
- [Ontology demand signal](https://clawhub.ai/skills/ontology)
- [Sprint Planning - 2026/08/31 (Week 36)](https://github.com/nisyuu/makasete-ai/issues/281)
- [Skills Weekly 2026-08-17 ClawHub Popular Skills Top 10](https://github.com/shufanli/AI-Product-Compass/issues/48)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, code snippets, shell commands, or configuration fragments depending on the user request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include visible assumptions, validation notes, and remaining risks when helpful.]

## Skill Version(s):

0.20260831.40551 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
