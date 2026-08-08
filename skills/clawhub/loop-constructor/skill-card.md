## Description: <br>
Designs gated, machine-checkable loop runbooks for medium or large semi-autonomous AI coding tasks without executing the workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Loop Constructor to turn medium or large AI-coding tasks into gated agent-loop designs, including decision logs, machine-checkable JSON, and .loop runbooks for later review and execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated .loop runbooks may later be used to run autonomous or semi-autonomous workflows. <br>
Mitigation: Review generated .loop files before running them, especially restart routes, and use an isolated workspace with version-control checkpoints. <br>
Risk: A structurally valid loop design can still contain weak checks or misleading stop conditions. <br>
Mitigation: Use the skill's linter and fresh-reader review pass before relying on a generated runbook. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vincentjiang06/skills/loop-constructor) <br>
- [SKILL.md](SKILL.md) <br>
- [README.en.md](README.en.md) <br>
- [The loop-selection procedure](references/loop-selection.md) <br>
- [Canonical loop-design shape](references/loop-design-shape.md) <br>
- [The operating model behind the shape](references/loops-model.md) <br>
- [loop-principle map](references/loop-principle-map.md) <br>
- [fresh-reader-checklist.md](assets/fresh-reader-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown report with JSON design artifacts and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces reviewable .loop runbooks and validation-oriented design files; it does not execute the designed autonomous workflow.] <br>

## Skill Version(s): <br>
0.3.0 (source: SKILL.md frontmatter, CHANGELOG.md, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
