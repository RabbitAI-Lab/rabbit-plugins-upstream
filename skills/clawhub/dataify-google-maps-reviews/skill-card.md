## Description:

Collect reviews and comments for a known Google Maps place URL. Do not use for place discovery or general place details without reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify collection tasks for reviews from a known Google Maps place URL and retrieve the collected JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the target Google Maps URL, review time range, and Dataify API token to Dataify.

Mitigation: Use a Dataify token appropriate for this tool and prefer temporary environment setup unless persistent shell storage is intentional.

Risk: Collection tasks may consume Dataify credits, especially for high-volume, multi-page, or multi-input requests.

Mitigation: Confirm consequential scope choices before submission and preserve the returned task ID so timed-out monitoring can resume without resubmitting a paid task.

Risk: The skill is scoped to reviews for a known place URL or identifier and is not intended for place discovery.

Mitigation: Resolve and verify the Google Maps place separately before using this skill for review collection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-maps-reviews)
- [Dataify builder endpoint](https://scraperapi.dataify.com/builder?platform=1)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID and resume command when asynchronous monitoring times out or is interrupted.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
