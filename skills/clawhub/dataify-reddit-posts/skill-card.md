## Description:

Collect Reddit posts by post URL, keyword, or subreddit URL; do not use when only comments from a known post are required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to submit Dataify collection jobs for Reddit posts by post URL, keyword, or subreddit URL, then monitor the asynchronous task and return the collected result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires DATAIFY_API_TOKEN and sends authenticated requests to Dataify.

Mitigation: Use a dedicated token, store it only as DATAIFY_API_TOKEN when needed, and never print or paste the token into chat.

Risk: Reddit URLs, subreddit URLs, or keywords are sent to Dataify for collection.

Mitigation: Review collection targets before execution and avoid high-volume or sensitive searches unless that scope is intentional.

Risk: Dataify collection jobs may consume account credits.

Mitigation: Confirm mode, targets, and num_of_posts before large or multi-input runs.

Risk: Asynchronous collection can time out or be interrupted after a paid task is submitted.

Mitigation: Keep the returned task_id and resume monitoring rather than submitting the same job again.

## Reference(s):

- [Mode and parameter reference](references/modes-and-parameters.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-reddit-posts)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON task or collection results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task_id/status summary or the final collected JSON result; default task monitoring waits up to 600 seconds.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
