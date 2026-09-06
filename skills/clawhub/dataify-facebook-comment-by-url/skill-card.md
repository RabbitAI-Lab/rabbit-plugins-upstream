## Description:

Collect comments from a known Facebook post URL. Do not use for the post body, personal profiles, or events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify jobs that collect comments from known Facebook post URLs, monitor the asynchronous task, and return the collected result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill submits authenticated Facebook post-comment collection jobs to Dataify using DATAIFY_API_TOKEN.

Mitigation: Configure DATAIFY_API_TOKEN out of band as an environment variable and do not paste the token into chat.

Risk: Security evidence reports that credential handling and automatic invocation controls are not consistently scoped.

Mitigation: Review before installing and consider disabling implicit invocation or requiring confirmation before authenticated collection jobs are submitted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-facebook-comment-by-url)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task or result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a submitted task_id, task status, or the final collected JSON result depending on wait behavior and task completion.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
