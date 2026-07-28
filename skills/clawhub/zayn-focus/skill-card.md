## Description: <br>
检查任务是否被做得过于复杂，并找出可复用资源、最小可用版本、应暂停事项和下一步。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People using WorkFn-style productivity prompts use this skill to decide whether a task has become too complex, identify reusable resources, define a minimum viable version, pause unnecessary expansion, and choose the next action. It is intended for situations where the user can provide core materials, a clear analysis goal, and at least one reliable source of evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is Chinese-language and marked as draft in the artifact documentation, so users may misunderstand scope or maturity. <br>
Mitigation: Review the source prompts and examples before use, and confirm the language and draft status are acceptable for the intended workflow. <br>
Risk: The skill can produce misleading plans if the user provides incomplete, conflicting, or weak evidence. <br>
Mitigation: Require the parameter status check first, ask for missing or conflicting inputs, and keep unsupported conclusions marked as preliminary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-focus) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with a parameter status table, task analysis, reusable resources, minimum viable version, pause list, and next step.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires enough user-provided task context and evidence before producing a formal analysis; otherwise it asks for missing information or labels the result as preliminary.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documents v0.1/0.1.0 draft status) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
