## Description:

Collect Amazon product reviews from one or more known product URLs. Use for Amazon review or comment extraction. Do not use for product details, product lists, or seller profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify jobs that collect Amazon product reviews from known product URLs and retrieve the resulting JSON. It is not intended for product details, product lists, or seller profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses DATAIFY_API_TOKEN to submit external Dataify requests.

Mitigation: Store the token in the environment, never paste it into chat, and verify only that it is present without printing its value.

Risk: Ambiguous, high-volume, multi-page, or media-related collection requests can increase credit use or runtime.

Mitigation: Review material ambiguities and high-volume scopes before execution; return the task ID and a resume path instead of resubmitting if monitoring times out.

Risk: The skill is scoped to Amazon review collection and may be misapplied to other Amazon data tasks.

Mitigation: Use it only with known Amazon product URLs for reviews or comments, and do not use it for product details, product lists, or seller profiles.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-amazon-comment)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify API token login](https://dashboard.dataify.com/login?utm_source=skill)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON results with concise Markdown guidance and shell commands when setup is required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN and a known Amazon product URL; may wait for asynchronous task completion.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
