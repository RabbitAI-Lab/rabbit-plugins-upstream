## Description:

Enables agents to submit and query a7w digital-human lip-sync jobs with a user-provided api.a7w.cn API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to generate lip-synced digital-human videos by submitting an audio URL and source video URL, then querying the asynchronous task result through the a7w API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included client can access more than the lipsync wrapper because it is a general a7w marketplace command-line client.

Mitigation: Review intended commands before installation and use it only when broad a7w marketplace access is acceptable.

Risk: The client reads a user-provided API key and can send it to the configured a7w host.

Mitigation: Use a dedicated low-balance API key, do not commit the key, and avoid overriding the default host unless the endpoint is trusted.

Risk: Submitted audio and video URLs are shared with the external a7w service and async submissions can be billable.

Mitigation: Submit only media URLs appropriate for third-party processing, confirm account balance and pricing, and avoid duplicate submissions.

## Reference(s):

- [Getting Started](references/getting-started.md)
- [Submit API](references/api-submit.md)
- [Query API](references/api-query.md)
- [Common Usage and Limits](references/通用说明.md)
- [a7w Compute Marketplace](https://api.a7w.cn/)
- [a7w AI Plugin Market](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown instructions with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task IDs, task status, generated video URLs, usage points, and error details from the a7w service.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
