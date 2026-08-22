## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical ontology-style workflows, checklists, analyses, and implementation support for work-productivity tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn ontology-style work-productivity requests into local-hardware-friendly plans, artifacts, checklists, analyses, code changes, or decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may cause the skill to activate for generic knowledge, graph, structured, creating, or bug-fix requests.

Mitigation: Prefer explicit ontology or typed-workflow requests when invoking the skill, and narrow trigger wording before deployment in environments with many installed skills.

Risk: Workflow guidance could be applied without enough project context, leading to incomplete or misleading plans.

Mitigation: Require the agent to state assumptions, constraints, success criteria, validation steps, and remaining risks in the final output.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-ontology-typed-workflow-helper)
- [Self-Improving + Proactive Agent Demand Signal](https://clawhub.ai/skills/self-improving)
- [Ontology Demand Signal](https://clawhub.ai/skills/ontology)
- [Ask HN: Release Notes Specificity](https://news.ycombinator.com/item?id=49367131)
- [OntologyOps Complete Solution](https://segmentfault.com/a/1190000047947726)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and next steps.]

## Skill Version(s):

0.20260821.52309 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
