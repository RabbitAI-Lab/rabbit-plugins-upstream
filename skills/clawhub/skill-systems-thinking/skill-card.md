## Description: <br>
Thinking-mode skill for LLMs that applies control-theoretic and systems-theoretic reasoning to software architecture, debugging, refactoring, and robustness work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shrimpleon](https://clawhub.ai/user/shrimpleon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI coding agents use this skill to reason through non-trivial software changes before acting: identify controlled variables, observe behavior, model uncertainty, stabilize the system, and close the loop with tests or other feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can link the skill into user-selected AI-agent skill directories and --force can replace an existing skill link. <br>
Mitigation: Review the installer targets before confirming installation and use --force only when intentionally replacing an existing link. <br>
Risk: The skill shapes agent reasoning and may slow or over-structure simple tasks if loaded unnecessarily. <br>
Mitigation: Use it for architecture, debugging, refactoring, and robustness work where explicit state, observability, bounds, and feedback checks are useful. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shrimpleon/skills/skill-systems-thinking) <br>
- [Closed-Loop Workflow](references/closed-loop-workflow.md) <br>
- [State, Control, Observability & Bounds](references/state-and-control.md) <br>
- [Stability](references/stability.md) <br>
- [Modeling & Engineering Approximation](references/modeling.md) <br>
- [Multivariable: Decouple What Hurts, Coordinate What Helps](references/multivariable.md) <br>
- [Disturbance Compensation & Time-Delay](references/disturbance.md) <br>
- [Time-Optimal & Bounded Control](references/bounded-control.md) <br>
- [Discrete / Sampled Systems & Test Cadence](references/discrete-systems.md) <br>
- [Possibility Space & Conjugate Control](references/possibility-space.md) <br>
- [Black-Box Epistemology](references/black-box-epistemology.md) <br>
- [Information and Control](references/information-and-control.md) <br>
- [System Evolution](references/system-evolution.md) <br>
- [Original Text Grounding](references/original-text.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with optional shell commands and reusable checklist or proposal templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a reasoning scaffold for agent behavior; it does not produce executable application code by itself.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
