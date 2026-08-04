## Description: <br>
Cybernetic Thinking is a thinking-mode skill that helps AI coding agents reason about complex software changes through control-theoretic concepts such as state, observability, stability, bounded control, coupling, and closed-loop feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shrimpleon](https://clawhub.ai/user/shrimpleon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI coding-agent users use this skill when designing architecture, debugging intermittent behavior, refactoring coupled modules, or making changes where correctness and robustness must be verified through observation and feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can link the skill into multiple agent directories after user confirmation. <br>
Mitigation: Install only from a trusted source and review the npx installer prompts before approving target agents. <br>
Risk: Removal examples that use rm -rf can delete unintended files if copied with the wrong path. <br>
Mitigation: Verify the exact old skill directory first or rename it to a backup before deletion. <br>
Risk: The PowerShell ExecutionPolicy Bypass verification example can bypass local execution restrictions. <br>
Mitigation: Prefer the normal pwsh verification command when possible and inspect the script before using a bypass option. <br>
Risk: The retry and backoff example is conceptual and may be unsafe if copied directly into production systems. <br>
Mitigation: Use the example as reasoning guidance only and design production retry behavior with explicit bounds, damping, and tests. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/shrimpleon/skills/skill-cybernetic-thinking) <br>
- [GitHub Repository](https://github.com/ShrimpLeon/cybernetic-thinking.git) <br>
- [Gitee Repository](https://gitee.com/leon0903/cybernetic-thinking.git) <br>
- [Closed-Loop Workflow & Analysis-before-Synthesis](references/closed-loop-workflow.md) <br>
- [State, Control, Observability & Bounds](references/state-and-control.md) <br>
- [Stability](references/stability.md) <br>
- [Modeling & Engineering Approximation](references/modeling.md) <br>
- [Multivariable - Decouple What Hurts, Coordinate What Helps](references/multivariable.md) <br>
- [Disturbance Compensation & Time-Delay](references/disturbance.md) <br>
- [Time-Optimal & Bounded Control](references/bounded-control.md) <br>
- [Discrete / Sampled Systems & Test Cadence](references/discrete-systems.md) <br>
- [Possibility Space & Conjugate Control](references/possibility-space.md) <br>
- [Black-Box Epistemology](references/black-box-epistemology.md) <br>
- [Information and Control - The Mutual Dependence](references/information-and-control.md) <br>
- [System Evolution - Stable States, Ultra-Stability, Catastrophe](references/system-evolution.md) <br>
- [Original Text - Engineering Cybernetics](references/original-text.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with optional code, shell command, configuration, checklist, and change-proposal content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes self-audit checks and reusable templates for debugging and planning; no API keys or external tool credentials are required.] <br>

## Skill Version(s): <br>
0.4.0 (source: SKILL.md frontmatter, CHANGELOG.md, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
