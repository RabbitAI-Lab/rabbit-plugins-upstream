## Description:

Skyvern (skyvern.com). Use this skill for ANY Skyvern request — reading, creating, and updating data. Whenever a task involves Skyvern, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run and manage Skyvern browser automation tasks through an OOMOL-connected account, including listing runs, inspecting run output, starting tasks, and canceling active runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Starting a Skyvern automation run can change external browser state even when the action is not labeled as write in the skill.

Mitigation: Review the exact run_task target and payload with the user before execution.

Risk: Canceling a run changes Skyvern state and may stop an active task or workflow.

Mitigation: Confirm the run identifier and intended effect before calling cancel_run.

Risk: The skill is a coherent Skyvern connector, but it under-labels starting a Skyvern automation as safe to run directly, so users should review actions before use.

Mitigation: Install only if you intend agents to operate your Skyvern account through OOMOL. Before allowing `run_task` or `cancel_run`, verify the exact target and payload yourself, because starting a browser automation run is not just a read-only action even though the skill does not mark it as write.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-skyvern)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Skyvern homepage](https://www.skyvern.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
