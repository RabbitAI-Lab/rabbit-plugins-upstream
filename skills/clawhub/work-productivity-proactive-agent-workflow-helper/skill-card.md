## Description:

Helps AI-agent users, skill authors, maintainers, and teams turn Proactive Agent-style workflow demand into practical plans, checklists, artifacts, analysis, or implementation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, agent users, skill authors, maintainers, and teams use this skill to clarify workflow requirements, produce local-hardware-friendly plans or artifacts, and verify outputs against success criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger language and implicit invocation may cause the helper to activate on general productivity or workflow prompts.

Mitigation: Invoke the skill explicitly when its planning workflow is desired, and narrow triggers before deployment if broad auto-activation is not acceptable.

Risk: The helper can produce plans, checklists, code changes, shell commands, or configuration guidance that may be incomplete or mismatched to the user's environment.

Mitigation: Review generated outputs against the stated success criteria and validate commands, code, or configuration in a controlled environment before use.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-proactive-agent-workflow-helper)
- [Popular ClawHub skill demand: Proactive Agent](https://clawhub.ai/skills/proactive-agent)
- [Popular ClawHub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving)
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code, shell command, configuration, checklist, or workflow sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, limits, validation notes, and remaining follow-up work when helpful.]

## Skill Version(s):

0.20260906.40422 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
