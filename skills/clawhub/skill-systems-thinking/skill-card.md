## Description: <br>
Systems Thinking is a thinking-mode skill that helps LLM coding agents apply a control-systems lens to architecture, debugging, refactoring, and other non-trivial code changes before acting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shrimpleon](https://clawhub.ai/user/shrimpleon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to make an agent identify system state, observability, stability, bounds, coupling, and verification loops before proposing or changing code. It is intended for architecture design, intermittent debugging, cross-module refactoring, and changes where correctness and robustness both matter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can link the skill into every detected supported agent, and --force can replace an existing same-named installation. <br>
Mitigation: Use installer flags such as --agents, --global, --local, or --all to restrict the target agents and locations, and avoid --force unless replacement is intended. <br>
Risk: The disturbance retry example is conceptual and may be unsafe if copied directly into a production retry path. <br>
Mitigation: Treat the example as reasoning guidance; add bounded retries, damping, tests, and environment-specific review before implementation. <br>


## Reference(s): <br>
- [Closed Loop Workflow](references/closed-loop-workflow.md) <br>
- [State and Control](references/state-and-control.md) <br>
- [Stability](references/stability.md) <br>
- [Modeling](references/modeling.md) <br>
- [Multivariable Systems](references/multivariable.md) <br>
- [Disturbance](references/disturbance.md) <br>
- [Bounded Control](references/bounded-control.md) <br>
- [Discrete Systems](references/discrete-systems.md) <br>
- [Original Text Grounding](references/original-text.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional shell commands and template content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces reasoning scaffolds, planning/checklist templates, and installation guidance rather than application runtime code.] <br>

## Skill Version(s): <br>
0.2.0 (source: SKILL.md frontmatter, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
