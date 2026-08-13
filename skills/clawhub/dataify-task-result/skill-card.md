## Description:

Download the JSON result for a completed Dataify scraper task by task ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve the JSON result for a completed Dataify scraper task after confirming the task ID and completion status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses DATAIFY_API_TOKEN to access Dataify task results.

Mitigation: Keep the token in the environment, do not paste it into chat or command arguments, and rely on the script's redaction behavior for output.

Risk: Returned JSON may contain scraped data that should not be shown or stored in every context.

Mitigation: Review the task ID and intended display or storage location before returning or saving the response.

Risk: Downloading the wrong or unfinished task can return an irrelevant provider response.

Mitigation: Use the skill after a successful Dataify task-status result unless the user explicitly requests direct retrieval.

## Reference(s):

- [Task Result API](references/task_result_api.md)
- [Dataify task result skill page](https://clawhub.ai/dataify-server/skills/dataify-task-result)
- [Dataify publisher profile](https://clawhub.ai/user/dataify-server)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [JSON response text with optional Markdown shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DATAIFY_API_TOKEN from the environment and redacts the token from script output.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
