## Description:

Helps agent users, skill authors, maintainers, and teams turn proactive-agent workflow demand into practical plans, checklists, analyses, code changes, and validation notes for improving reliability and safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, agent users, skill authors, maintainers, and teams use this skill to adapt popular proactive-agent workflow patterns into concrete local workflows, artifacts, code changes, and decision support. It is intended for tasks such as bug fixing, setup hardening, safety review, reliability improvement, and creating adjacent skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad trigger wording and implicit invocation is enabled, so it may be selected for ordinary productivity or task requests.

Mitigation: Prefer explicit invocation or narrow the trigger language when tighter routing behavior is required.

Risk: The skill can produce workflow guidance, code changes, or decision support that may be incorrect or incomplete for the user's environment.

Mitigation: Review outputs against stated success criteria, scan code changes before deployment, and keep assumptions and remaining risks visible.

## Reference(s):

- [Requirement Plan](artifact/references/requirement-plan.md)
- [Published ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-proactive-agent-workflow-helper)
- [Popular ClawHub skill demand: Proactive Agent](https://clawhub.ai/skills/proactive-agent)
- [Popular ClawHub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving)
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, or code snippets depending on the requested artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include checklists, work plans, verification notes, assumptions, and follow-up risks.]

## Skill Version(s):

0.20260810.40316 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
