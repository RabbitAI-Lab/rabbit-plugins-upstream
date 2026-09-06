## Description:

Collect structured Booking.com hotel records from a known Booking hotel or listing URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit known Booking.com hotel or listing URLs to Dataify and return collected Booking hotel records. It is suited for hotel detail or listing extraction when the target Booking URL is already known.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied Booking.com URLs are sent to Dataify and collection tasks may consume Dataify credits.

Mitigation: Set DATAIFY_API_TOKEN outside chat, review the target URL and collection scope before larger or multi-URL jobs, and resume existing task IDs instead of resubmitting paid tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-booking-hotellist)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON results or Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Booking.com URL and a Dataify API token; waits up to 600 seconds for final results by default.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
