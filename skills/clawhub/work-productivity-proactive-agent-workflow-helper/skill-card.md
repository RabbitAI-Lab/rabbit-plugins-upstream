## Description:

Helps agent users, skill authors, maintainers, and teams turn proactive-agent workflow demand into practical plans, checklists, implementation support, and verification notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and agent teams use this skill to clarify productivity workflow requests, produce concrete artifacts such as plans or checklists, and verify the result against the user's success criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers and implicit invocation can make the skill activate for ordinary productivity or bug-fix requests where it is not the best match.

Mitigation: Review activation behavior after installation and narrow triggers or invocation policy when precise routing is important.

Risk: Generated workflow, checklist, code, or configuration guidance can be incomplete or mismatched to the user's environment.

Mitigation: Validate outputs against the stated success criteria before applying them and keep assumptions, limits, and required inputs visible.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Proactive Agent demand signal](https://clawhub.ai/skills/proactive-agent)
- [Self-Improving + Proactive Agent demand signal](https://clawhub.ai/skills/self-improving)
- [Ontology demand signal](https://clawhub.ai/skills/ontology)
- [ClawHub popular skills issue](https://github.com/shufanli/AI-Product-Compass/issues/48)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code blocks, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should expose assumptions, limits, required inputs, remaining risks, and follow-up work when relevant.]

## Skill Version(s):

0.20260828.40337 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
