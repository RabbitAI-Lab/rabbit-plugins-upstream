## Description: <br>
Design and implement Oban background job workers for Elixir, including queue configuration, retry strategies, uniqueness constraints, cron scheduling, error handling, worker code, queue config, and test setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gchapim](https://clawhub.ai/user/gchapim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill when adding background jobs, asynchronous processing, scheduled tasks, recurring cron jobs, or Oban worker tests to Elixir applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated webhook worker examples may send payloads to untrusted or incorrect destinations. <br>
Mitigation: Validate webhook destinations, sign requests, avoid sending unnecessary sensitive fields, and review retry behavior before production use. <br>
Risk: Cleanup and import worker examples can delete or bulk-write application data if adapted without scoping. <br>
Mitigation: Scope cleanup deletes carefully, restrict import file paths or use upload IDs, and test bulk-write jobs with rollback or dry-run plans. <br>


## Reference(s): <br>
- [Testing Oban Workers Reference](references/testing-oban.md) <br>
- [Worker Patterns Reference](references/worker-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Elixir and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces documentation-style implementation guidance and examples for Oban workers, tests, and configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
