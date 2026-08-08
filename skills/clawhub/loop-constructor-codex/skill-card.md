## Description: <br>
Designs engineered gated loops for medium or large semi-autonomous AI-coding tasks on the Codex CLI and emits runnable `.loop/` runbooks without executing them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design a staged, machine-checkable Codex workflow for a substantial coding task before an agent executes it. It produces a `.loop/` runbook, loop-design JSON, decision log, contract, and verification steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated runbooks can include `codex exec`, git worktree, or check commands that may modify a target repository when an operator later runs them. <br>
Mitigation: Review generated runbooks and commands before execution, and use the intended sandbox and approval settings for later operator steps. <br>
Risk: The skill writes design artifacts, usually under `.loop/`, into the project where it is used. <br>
Mitigation: Install and invoke it only when project-local `.loop/` artifacts are desired, then review the generated files before adopting the runbook. <br>


## Reference(s): <br>
- [Codex CLI runtime mapping](references/codex-runtime.md) <br>
- [Canonical loop-design shape](references/loop-design-shape.md) <br>
- [loop-principle map - 9 steps to KB grounding](references/loop-principle-map.md) <br>
- [The loop-selection procedure (D0-D6)](references/loop-selection.md) <br>
- [The operating model behind the shape (LOOPS.md)](references/loops-model.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown plus JSON loop-design files and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces bounded `.loop/` artifacts and design/runbook guidance; it does not execute the designed loop.] <br>

## Skill Version(s): <br>
0.2.0 (source: server evidence, frontmatter, changelog released 2026-07-31) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
