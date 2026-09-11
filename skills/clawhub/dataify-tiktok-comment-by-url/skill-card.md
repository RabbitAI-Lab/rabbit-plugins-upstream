## Description:

Prepares and submits Dataify Builder requests for TikTok URL-based collection workflows, including the advertised TikTok comment-by-URL tool and related saved catalog entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to collect TikTok data from known URLs through Dataify, submit the asynchronous task, monitor completion, and return the final JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted targets and collected results are sent to Dataify.

Mitigation: Use the skill only when Dataify processing is acceptable for the target data and result content.

Risk: The artifact includes related TikTok scraper entries beyond the advertised comment-by-URL workflow.

Mitigation: Restrict use to the intended TikTok comment workflow unless broader TikTok collection has been reviewed and approved.

Risk: API-token handling and query-string polling can expose credentials in local logs or command history.

Mitigation: Use a session-scoped Dataify token, avoid printing token-bearing URLs, and rotate any token that may have been exposed.

Risk: Normal submissions may consume paid Dataify credits.

Mitigation: Require confirmation before paid or high-volume submissions and use preview or no-wait behavior only when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-tiktok-comment-by-url)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder)
- [Tool parameter catalog](artifact/references/tool-params.json)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task/result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit paid Dataify tasks, wait for asynchronous completion, and summarize large result payloads while preserving access to raw JSON.]

## Skill Version(s):

1.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
