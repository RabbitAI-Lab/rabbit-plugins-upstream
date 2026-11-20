## Description:

仅在用户要求同步某个 spec 或功能的开发上下文（如“同步下 spec009 的开发上下文”），或要求更新 quickstart 时使用。同步时若接手点过时，先追到最新进度并回写，再接续工作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-zh](https://clawhub.ai/user/peterflow-zh)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to verify or refresh a feature's handoff notes against the original task and recent evidence, then continue from the current next step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A stale handoff note could direct an agent to a completed step or miss a changed prerequisite.

Mitigation: Check the recorded next step against the original task and recent evidence; refresh the note when the status or prerequisites have changed.

## Reference(s):

- [ClawHub quickstart skill page](https://clawhub.ai/peterflow-zh/skills/quickstart)
- [Quickstart handoff template](assets/quickstart.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown handoff note and concise task context]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
