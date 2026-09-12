## Description:

Collect Amazon product-list records by keyword and marketplace domain when list-style Amazon results from a target domain are required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Builder jobs that collect Amazon product-list records for a keyword and marketplace domain, then monitor the task and return the final JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataify API tokens, keywords, domains, task IDs, and result requests may be exposed to Dataify or the workflow.

Mitigation: Use an isolated environment with a dedicated Dataify token, avoid confidential inputs, and rotate the token if exposure is suspected.

Risk: The primary script can import runtime code from outside the reviewed skill package.

Mitigation: Run the skill away from untrusted sibling packages and review the resolved import path before installation or execution.

Risk: The package bundles broader scraping helpers beyond the Amazon product-list use case.

Mitigation: Constrain use to Amazon product-list collection and remove unrelated scraping helpers before deployment.

Risk: API tokens may be placed in URL query strings during task status and download requests.

Mitigation: Prefer secure token transport, avoid logging request URLs, and redact tokens from any retained diagnostics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-amazon-product-list)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit asynchronous Dataify tasks and return task IDs, resume commands, or final JSON results.]

## Skill Version(s):

1.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
