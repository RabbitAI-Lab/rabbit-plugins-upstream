## Description:

Create new skills, modify and improve existing skills, and measure skill performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and skill authors use this skill to draft, revise, evaluate, benchmark, optimize, and package agent skills through an iterative review workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review viewer can terminate another local process that is listening on the selected port.

Mitigation: Use the static viewer mode when possible, or choose and verify an unused port before starting the localhost server.

Risk: Normal workflows can edit local skill files, run evaluation scripts and subagents, invoke the local claude CLI, start localhost review servers, and write review or benchmark artifacts.

Mitigation: Install and run the skill in a project-scoped workspace first, review generated commands and files before execution, and keep work in disposable iteration directories until approved.

Risk: Generated or revised skill instructions can introduce inaccurate or misleading guidance.

Mitigation: Review generated skill content, evaluation results, and scan output before packaging or deploying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/skill-creator)
- [Skill Creator schemas](references/schemas.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON examples, shell commands, generated skill files, evaluation artifacts, benchmark reports, and packaged .skill archives]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write SKILL.md, eval metadata, grading results, benchmark JSON/Markdown, static HTML review pages, feedback JSON, and packaged skill archives during normal workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
