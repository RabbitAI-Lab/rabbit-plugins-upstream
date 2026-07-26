## Description: <br>
Multi-step scheduler for in-depth agent requests. Detects when user needs multiple steps, suggests plan and waits for confirmation, persists state, and runs heartbeat-aware flow. Use when requests have 3+ actions, sequential dependencies, output dependencies, or high scope/risk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gostlightai](https://clawhub.ai/user/gostlightai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to break larger approved requests into sequenced steps, persist state, retry failures, and continue work through heartbeat-driven checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Heartbeat automation can continue approved multi-step work after the initial interaction. <br>
Mitigation: Review the generated plan before sensitive work, disable the heartbeat when automation should stop, or mark the state DONE. <br>
Risk: The runner invokes a local agent through STEP_AGENT_CMD. <br>
Mitigation: Set STEP_AGENT_CMD and STEP_RUNNER only to trusted local commands or paths. <br>
Risk: Step instructions and state files may expose sensitive task details if secrets are included. <br>
Mitigation: Avoid placing secrets in step instructions and review persisted state before sharing logs or artifacts. <br>


## Reference(s): <br>
- [Agent Step Sequencer State Schema](references/state-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands, JSON] <br>
**Output Format:** [Markdown guidance with JSON state examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and STEP_AGENT_CMD; may persist state.json and record per-step output summaries.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence and changelog, released 2026-02-10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
