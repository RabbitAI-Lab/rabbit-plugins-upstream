## Description:

Collect comments from a known Instagram post URL. Do not use for profile data or Reel details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Instagram post-comment collection jobs for specific Instagram post URLs, monitor the returned task, and receive the final collected result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Dataify API TOKEN to submit Dataify collection jobs.

Mitigation: Install only when comfortable allowing the skill to use DATAIFY_API_TOKEN, and do not expose the token in chat or output.

Risk: Submitted Dataify jobs may consume Dataify credits.

Mitigation: Review high-volume or multi-post collection scope before execution and avoid resubmitting paid tasks when a task_id is already available.

Risk: The skill is scoped to user-provided Instagram post URLs.

Mitigation: Provide actual Instagram post URLs and reject URLs outside https://www.instagram.com/.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-instagram-comment-by-posturl)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder?platform=1)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task/result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN and an Instagram post URL; waits for the final result by default unless no-wait behavior is requested.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
