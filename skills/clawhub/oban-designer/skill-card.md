## Description: <br>
Design and implement Oban background job workers for Elixir. Configure queues, retry strategies, uniqueness constraints, cron scheduling, and error handling. Generate Oban workers, queue config, and test setups. Use when adding background jobs, async processing, scheduled tasks, or recurring cron jobs to an Elixir project using Oban. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gchapim](https://clawhub.ai/user/gchapim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to design Oban background job workers for Elixir applications, including queue configuration, retry behavior, uniqueness, cron scheduling, monitoring, and tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The examples include network, file, and database worker patterns that may be unsafe if copied into production without project-specific controls. <br>
Mitigation: Validate webhook destinations, avoid raw user-controlled URLs or filesystem paths in job arguments, keep secrets out of job data, and narrowly scope database writes and deletes. <br>
Risk: Queue, retry, and cron snippets can create excess load or repeated side effects when schedules and retry behavior are not tested. <br>
Mitigation: Test cron schedules before enabling them, make workers idempotent where practical, use uniqueness constraints for duplicate-prone jobs, and monitor queue depth, error rate, and retry rate. <br>


## Reference(s): <br>
- [Worker Patterns Reference](references/worker-patterns.md) <br>
- [Testing Oban Workers Reference](references/testing-oban.md) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Elixir and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
