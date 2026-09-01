## Description:

Schedule a social media post for a future time through PostLake, and list, reschedule, or cancel scheduled posts. Use when the user wants to post later or plan a calendar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[postlake](https://clawhub.ai/user/postlake)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams use this skill to prepare a social posting calendar through PostLake, including scheduling, reviewing, rescheduling, and canceling future posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, edit, and cancel public social content using the user's PostLake API key.

Mitigation: Ask the agent to summarize the target post, account, and scheduled time before any edit or cancellation.

## Reference(s):

- [PostLake API base URL](https://api.postlake.dev)
- [PostLake posts endpoint](https://api.postlake.dev/v1/posts)
- [PostLake scheduled posts query](https://api.postlake.dev/v1/posts?state=scheduled)
- [PostLake schedule skill on ClawHub](https://clawhub.ai/postlake/skills/postlake-schedule)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires POSTLAKE_API_KEY and user confirmation of the target post, account, and scheduled time before edits or cancellations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
