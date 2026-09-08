## Description:

Collect a Facebook post and structured post data from a known post URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify collection jobs for one or more Facebook post URLs and retrieve the final structured result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A clear collection request may use a saved DATAIFY_API_TOKEN and spend Dataify credits.

Mitigation: Run the skill only for intended Facebook post URLs and confirm materially larger or ambiguous collection scopes before execution.

Risk: The supplied Facebook post URL and task parameters are sent to Dataify for collection.

Mitigation: Avoid submitting private, sensitive, or unauthorized URLs and review account access requirements before use.

Risk: Asynchronous collection can time out after task submission.

Mitigation: Preserve the returned task ID and resume monitoring instead of resubmitting the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-facebook-post-by-url)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task or result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit Dataify collection jobs and wait for asynchronous task completion.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
