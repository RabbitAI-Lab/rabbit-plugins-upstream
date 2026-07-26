## Description: <br>
3-Agent competitive loop with Planner/Generator/Evaluator and Sprint Contract. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wljmmx](https://clawhub.ai/user/wljmmx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to structure software development tasks as a Planner/Generator/Evaluator loop with sprint contracts, acceptance criteria, competitive solution selection, and verification checkpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill broadly auto-activates for development tasks and can drive child-agent coding workflows that modify code. <br>
Mitigation: Install only when that workflow is intended, keep the human approval gates for contracts and final selection, and review generated changes before relying on them. <br>
Risk: The security summary notes an explicit preference for a no-audit model for unrestricted judgment. <br>
Mitigation: Review or remove the no-audit model preference and use organization-approved model routing before routine use. <br>
Risk: The workflow can spawn child sessions, persist task state, and consume local model or GPU resources. <br>
Mitigation: Review time budgets, session behavior, and local resource settings before deployment in shared or resource-constrained environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wljmmx/skills/competitive-agent-loop) <br>
- [REST API CRUD Example](examples/rest-api-example.md) <br>
- [Sprint Contract Template](templates/sprint-contract.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with structured reports, tables, YAML templates, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces sprint contracts, implementation summaries, acceptance proofs, evaluator scores, critiques, and documentation deliverables.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
