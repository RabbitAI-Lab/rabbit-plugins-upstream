## Description:

Process multiple items with progress tracking, checkpointing, and failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and agents use this skill to run batch operations with dry runs, progress reporting, checkpoints, retries, and partial failure recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Destructive batch operations can affect many items at once.

Mitigation: Run a small dry run first, confirm destructive actions before execution, snapshot state, log undo information, and offer rollback on abort.

Risk: Checkpoint and failed-item files may contain sensitive batch data.

Mitigation: Review where checkpoint or failure files will be written, keep them scoped to the task, and avoid exposing sensitive contents.

Risk: Timeouts, rate limits, or bad inputs can create partial failures.

Mitigation: Use retries with backoff for transient failures, throttle rate-limited APIs, log skippable errors, and abort fatal failures such as authentication or disk issues.

## Reference(s):

- [Batch Strategies](artifact/strategies.md)
- [Batch Error Handling](artifact/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code, command, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend temporary checkpoint or failure files for retries and recovery.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
