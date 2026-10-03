## Description:

Reviews Postify content calendars, identifies posting gaps and failed posts, and reschedules posts after user confirmation without publishing or deleting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers and other Postify users review scheduled, draft, published, and failed posts, find gaps by channel, and move scheduled posts after confirming the new time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Postify account exposes an organization's channels and posting schedule to the agent.

Mitigation: Connect only a trusted Postify account and grant access only when comfortable sharing the organization's calendar.

Risk: Moving a scheduled post to the wrong date or time could disrupt the posting plan.

Mitigation: Confirm the post ID and new time before rescheduling, then report the resulting datetime with its timezone.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bsalaeddin/skills/postify-managing-content-calendar)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown calendar summaries and rescheduling confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posts grouped by day and channel, with status and local times; no publishing or deleting.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
