## Description:

Download the JSON result of a completed Dataify scraper task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve JSON output for a known Dataify task ID after the task has completed successfully.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends DATAIFY_API_TOKEN to Dataify's download endpoint to retrieve task results.

Mitigation: Use a session-scoped DATAIFY_API_TOKEN environment variable, do not paste the token into chat, and install the skill only when Dataify result retrieval is intended.

## Reference(s):

- [Task Result API](references/task_result_api.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-task-result)
- [Dataify download endpoint](https://scraperapi.dataify.com/download)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON result content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads DATAIFY_API_TOKEN from the environment and redacts the token from dry-run and error output.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
