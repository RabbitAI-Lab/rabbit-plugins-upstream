## Description: <br>
Design an engineered gated loop for a medium or large semi-autonomous AI coding task executed with the Codex CLI, emitted as a runnable .loop runbook without executing the loop. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design check-gated Codex CLI runbooks for medium and large coding tasks, including decision logs, machine-checkable loop-design JSON, and runnable .loop documentation. It is for planning and persisting the loop design, not for executing the generated workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated runbooks may later guide powerful semi-autonomous Codex coding workflows. <br>
Mitigation: Review the generated .loop files, sandbox settings, checks, and human approval points before running any workflow. <br>
Risk: An incorrect or hollow stage check could let a generated loop appear complete while the implementation is still wrong. <br>
Mitigation: Run the bundled linter and perform the fresh-reader review of each check, falsifiable condition, passing-but-wrong case, contract assertion, and stop condition before use. <br>
Risk: Following generated Codex commands with excessive permissions could expand the workflow's blast radius. <br>
Mitigation: Use read-only evaluators, workspace-write generators, explicit human approval for host or production access, and avoid danger-full-access unless a reviewer accepts that risk. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/loop-constructor-codex) <br>
- [README](artifact/README.md) <br>
- [Codex CLI runtime mapping](artifact/references/codex-runtime.md) <br>
- [Loop selection procedure](artifact/references/loop-selection.md) <br>
- [Canonical loop-design shape](artifact/references/loop-design-shape.md) <br>
- [Operating model behind the shape](artifact/references/loops-model.md) <br>
- [Loop-principle map](artifact/references/loop-principle-map.md) <br>
- [Fresh-reader checklist](artifact/assets/fresh-reader-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown runbook plus machine-checkable JSON loop design with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes .loop/<slug>.loop.md and .loop/<slug>.loop.json after linting; design-only and does not execute the generated loop.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata; artifact frontmatter and changelog report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
