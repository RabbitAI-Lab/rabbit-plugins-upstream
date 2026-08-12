## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical self-improving and proactive-agent workflows for bug fixing, safety hardening, reliability improvements, and adjacent skill creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External agent users, skill authors, maintainers, and teams use this skill to turn self-improving and proactive-agent demand into concrete workflows, checklists, analysis, code changes, or decision support. It is intended for practical productivity work that clarifies goals, keeps assumptions visible, and validates the result against stated success criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger words and implicit invocation can cause the skill to activate in contexts where a narrower workflow helper was intended.

Mitigation: Invoke the skill explicitly by name or narrow its trigger configuration before using it in environments with many installed skills.

Risk: Workflow, checklist, code, or configuration proposals can be incorrect or poorly matched to the user's environment.

Mitigation: Review generated artifacts before applying them, keep assumptions visible, and validate results against the stated success criteria.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Skill release page](https://clawhub.ai/kyro-ma/skills/work-productivity-self-improving-workflow-helper)
- [Popular ClawHub skill demand: self-improving agent](https://clawhub.ai/skills/self-improving-agent)
- [Popular ClawHub skill demand: Proactive Agent](https://clawhub.ai/skills/proactive-agent)
- [Popular ClawHub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or text with optional code, shell command, checklist, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, limits, validation notes, and next steps when useful.]

## Skill Version(s):

0.20260812.40408 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
