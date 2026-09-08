## Description:

Check whether a known Dataify scraper task is processing, successful, or failed, with automatic completed-result retrieval when the task status is successful.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check the state of an existing Dataify scraper task ID and handle processing, success, or failure responses. When the status is successful, the bundled script automatically retrieves and prints the completed JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may display completed task data because a successful status triggers automatic JSON result retrieval.

Mitigation: Run it only for task IDs whose completed result may be shown in the agent output, or ask the publisher to separate status checking from result download.

Risk: The skill requires a Dataify API token and uses it for both status checks and successful-result downloads.

Mitigation: Provide the token only through DATAIFY_API_TOKEN, review account access before use, and do not paste credentials into chat or command arguments.

## Reference(s):

- [Task Status API](references/task_status_api.md)
- [Dataify task status endpoint](https://scraperapi.dataify.com/task_status)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON response bodies, with Markdown guidance when setup or error handling is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May automatically print completed task JSON when the task status is successful.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
