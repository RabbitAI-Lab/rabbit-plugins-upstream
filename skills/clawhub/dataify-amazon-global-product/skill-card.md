## Description:

Collects Amazon global-marketplace product data by product URL, category URL, keyword, or keyword plus brand through Dataify Builder.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Amazon global product collection jobs to Dataify, monitor the asynchronous task, and retrieve final JSON results. It is intended for requests involving multi-market Amazon product URLs, category URLs, keywords, or keyword plus brand filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Dataify API token and sends product URLs, keywords, brands, and task data to Dataify.

Mitigation: Use a scoped or replaceable token, avoid sensitive inputs, and confirm the collection target and scope before submission.

Risk: Server security evidence flags weak target scoping, broader scraping code, risky credential handling, and an unreviewed adjacent-code import path.

Mitigation: Run the skill in a constrained environment, avoid untrusted sibling directories, and review the shipped scripts before deployment.

Risk: Polling and task completion depend on remote Dataify endpoints and may time out after paid task submission.

Mitigation: Preserve the returned task ID and resume monitoring instead of resubmitting the same collection.

## Reference(s):

- [Dataify Amazon Global Product on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-amazon-global-product)
- [Publisher profile: dataify-server](https://clawhub.ai/user/dataify-server)
- [Modes and parameters](references/modes-and-parameters.md)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON task/result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN and sends selected Amazon targets, keywords, brands, and task parameters to Dataify.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
