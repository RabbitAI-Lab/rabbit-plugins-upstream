## Description:

Prevents agent stopped responding failures in sandboxed agent runtimes by giving agents a detach, bounded-poll, durable-state pattern and jobctl.sh command workflow for long-running or prompt-prone tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to keep long-running builds, downloads, installs, and model-inference tasks from blocking an agent turn. It guides agents to launch work in the background, poll with bounded waits, persist job state, resume idempotently, and verify final outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detached commands can continue running after the agent turn ends or is cancelled.

Mitigation: Review the exact command before launch, apply bounded timeouts, track job state, and clean up detached processes when work is finished.

Risk: Local job logs and state files may contain command output, inputs, or sensitive derived data.

Mitigation: Protect ~/.jobs and related logs, avoid sending secrets to commands that log output, and remove job state when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/nonblocking-agent-execution)
- [Artifact README](artifact/README.md)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces non-blocking execution patterns, background-job command examples, durable state conventions, and verification guidance for agent-run tasks.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
