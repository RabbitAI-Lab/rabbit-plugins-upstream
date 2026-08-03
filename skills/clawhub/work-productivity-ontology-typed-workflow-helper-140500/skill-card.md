## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical ontology-style workflows, checklists, analyses, and implementation support for work-productivity tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users, skill authors, maintainers, and teams use this skill to turn ontology-style workflow needs into actionable plans, templates, checklists, analyses, code changes, or decision support. It is aimed at practical bug fixing, setup hardening, reliability improvement, and adjacent workflow creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation keywords may invoke the skill more often than intended. <br>
Mitigation: Prefer explicit invocation by skill name or tighten activation wording before deployment in environments where unintended activation is a concern. <br>
Risk: Workflow or code guidance may be incomplete or misapplied to a specific user's repository or operational context. <br>
Mitigation: Review outputs against the stated success criteria, scan or test any generated code or configuration, and keep assumptions visible to the reviewer. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-ontology-typed-workflow-helper-140500) <br>
- [Popular ClawHub skill demand: self-improving agent](https://clawhub.ai/skills/self-improving-agent) <br>
- [Popular ClawHub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving) <br>
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology) <br>
- [Forked CozoDB to give agents cognitive primitives](https://news.ycombinator.com/item?id=48605896) <br>
- [OntologyOps complete plan](https://segmentfault.com/a/1190000047947726) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should be tailored to the user's immediate context and include assumptions, limits, validation steps, and remaining risks when useful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
