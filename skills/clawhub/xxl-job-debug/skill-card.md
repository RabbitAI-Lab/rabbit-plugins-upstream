## Description:

Use when triggering or debugging XXL-JOB tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jrd77](https://clawhub.ai/user/jrd77)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate and debug XXL-JOB scheduler tasks, including creating, updating, triggering, logging, killing, and deleting jobs through admin and executor APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide create, update, start, stop, kill, and delete operations against XXL-JOB scheduler jobs.

Mitigation: Review each requested operation before execution, especially in production, and provide only the specific job IDs and executor addresses needed for the task.

Risk: XXL-JOB access tokens and executor configuration are needed for API operations.

Mitigation: Provide only task-specific credentials and avoid printing or exposing full tokens in agent output.

Risk: Debugging against the wrong executor or creating persistent schedules can affect unintended jobs or environments.

Mitigation: Verify the target executor with the beat endpoint, prefer one-shot triggering with an explicit address list, and avoid persistent schedules unless requested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jrd77/skills/xxl-job-debug)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with HTTP, JSON, YAML, properties, Java, and text code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operation summaries may include job ID, app name, executor, handler, parameters, log ID, status, result, error stage, and evidence.]

## Skill Version(s):

4.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
