## Description:

Helps agent users, skill authors, maintainers, and teams create practical ontology-style workflows, checklists, analysis, implementation support, and reliability improvements for work-productivity use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, AI-agent users, skill authors, maintainers, and teams use this skill to turn ontology-style workflow needs into concrete plans, templates, checklists, analysis, code changes, or decision support. It is intended for practical work-productivity tasks that need clear constraints, local-hardware-friendly execution, and visible validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad workflow and knowledge-graph trigger wording and allows implicit invocation, so it may activate for adjacent prompts where a narrower skill would be preferable.

Mitigation: Review routing behavior before deployment and narrow trigger wording or disable implicit invocation when the platform lacks strong routing safeguards.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Popular Clawhub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving)
- [Popular Clawhub skill demand: ontology](https://clawhub.ai/skills/ontology)
- [Ask HN: How do you develop more deterministic LLM pipelines?](https://news.ycombinator.com/item?id=49293943)
- [OntologyOps complete solution](https://segmentfault.com/a/1190000047947726)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Code, Configuration, Shell commands]

**Output Format:** [Markdown prose with optional code blocks, checklists, templates, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, constraints, validation checks, remaining risks, and next steps when useful.]

## Skill Version(s):

0.20260815.40440 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
