## Description:

Collect Amazon seller profile and seller information from a known seller URL. Do not use for product details, listings, or reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Builder jobs for Amazon seller profile and seller information collection from a known seller URL, then monitor the asynchronous task and return the collected JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the target Amazon seller URL to Dataify's external service and successful submissions may consume Dataify credits.

Mitigation: Confirm the seller URL and intended collection before execution, especially for ambiguous, high-volume, or credit-sensitive requests.

Risk: The skill requires DATAIFY_API_TOKEN for authenticated Dataify access.

Mitigation: Keep DATAIFY_API_TOKEN private, verify only whether it is present, and never print or include the token in chat, logs, or generated output.

Risk: Submitting the same request again after an interruption can create duplicate paid tasks.

Mitigation: Reuse the returned task_id and resume monitoring instead of resubmitting when a run times out or is interrupted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-amazon-seller)
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify Login](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with JSON task summaries and final result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns final collected results by default; may return a task_id and resume command if monitoring is skipped, times out, or is interrupted.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
