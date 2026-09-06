## Description:

Collect Amazon product-list records by keyword and marketplace domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit Dataify Amazon product-list collection jobs for a keyword and marketplace domain, wait for asynchronous completion, and return collected JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting collection jobs uses a Dataify API token and may consume Dataify credits.

Mitigation: Use a dedicated Dataify API token and confirm collection scope, such as page count, before high-volume runs.

Risk: Persisting the Dataify API token on shared or untrusted machines could expose account credentials.

Mitigation: Prefer session-scoped token configuration on shared systems and never print or paste the token into chat.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-amazon-product-list)
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task/result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns task metadata and, by default, monitors the Dataify task for final JSON results.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
