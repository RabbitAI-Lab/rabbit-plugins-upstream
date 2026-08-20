## Description:

Autopilot runs a coding task end to end without mid-run human gates, making documented assumptions, editing and testing incrementally, reviewing blockers, and stopping before commits, pushes, or pull requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to run unattended codebase tasks from acquisition through planning, implementation, testing, blocker review, and final reporting. It is intended for hands-off runs where the agent should document assumptions and leave commits, pushes, and pull requests to a human.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform autonomous file edits and command execution for codebase tasks.

Mitigation: Install it only when hands-off code work is intended, use normal or edit-accepting permissions for routine runs, and review the final diff before committing or publishing.

Risk: Elevated permission modes can remove interactive safety checks during unattended execution.

Mitigation: Reserve bypass or dangerously-skip-permissions modes for disposable sandboxes and stop before commits, pushes, or pull requests.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with working-tree code and configuration changes, verification evidence, assumptions, and paste-ready handoff commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stops before committing, pushing, or creating pull requests; halts for destructive actions, missing access, or infeasible specifications.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
