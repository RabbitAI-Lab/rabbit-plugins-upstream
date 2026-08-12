## Description:

Check the execution status of a Dataify scraper task by task ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to check whether a Dataify Builder scraping task is processing, succeeded, or failed. When the provider reports success, the bundled workflow retrieves the task's JSON result for the agent to return.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Successful status checks automatically fetch and display the task's full JSON result, which may include sensitive scraped content.

Mitigation: Install and invoke the skill only when full result retrieval is acceptable; treat task IDs and outputs as sensitive and prefer a status-only flow when completion metadata is enough.

Risk: The skill requires a Dataify API token to query task status.

Mitigation: Provide the token only through DATAIFY_API_TOKEN, use dry-run mode for request previews, and avoid pasting credentials into chat or command arguments.

## Reference(s):

- [Task Status API](references/task_status_api.md)
- [Dataify Task Status on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-task-status)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown with shell command examples and JSON response bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DATAIFY_API_TOKEN from the environment and prints the downloaded JSON result when a task succeeds.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
