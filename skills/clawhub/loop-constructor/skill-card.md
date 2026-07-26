## Description: <br>
Design the engineered loop for a medium/large (semi-)autonomous AI-coding task by decomposing it into gated sub-loops, emitted as a runnable .loop/ runbook. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design gated agent loops for medium or large autonomous coding tasks. It produces a reviewable loop design and runnable .loop/ runbook without executing the designed workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated runbooks may encode an incorrect or unsuitable autonomous workflow. <br>
Mitigation: Review the generated runbook and loop-design JSON before using them to run any autonomous workflow. <br>
Risk: The skill runs local validation scripts and creates .loop files in the target project. <br>
Mitigation: Run it only in the intended workspace and review the resulting file changes before adopting them. <br>
Risk: Structural validation can pass while the loop's checks are too weak for the real task. <br>
Mitigation: Use the bundled fresh-reader checklist and require human review for consequential or hard-to-reverse workflows. <br>


## Reference(s): <br>
- [SKILL.md](SKILL.md) <br>
- [README.en.md](README.en.md) <br>
- [Loop Selection](references/loop-selection.md) <br>
- [Loop Design Shape](references/loop-design-shape.md) <br>
- [Loops Model](references/loops-model.md) <br>
- [Loop Principle Map](references/loop-principle-map.md) <br>
- [Fresh Reader Checklist](assets/fresh-reader-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON loop-design/runbook files and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes .loop runbook artifacts only after validation; it designs the loop and does not execute the designed workflow.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
