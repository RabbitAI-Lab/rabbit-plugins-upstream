## Description:

Prepares Dataify builder requests for TikTok comment-by-URL collection and related TikTok Dataify tools, then returns submission commands and collected results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and submit Dataify TikTok collection tasks from known URLs, monitor asynchronous task completion, and retrieve JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is broader than its TikTok-comments-only label because it can prepare and submit Dataify tasks for shops, post lists, and profiles.

Mitigation: Install only when broader TikTok Dataify builder authority is intended, or narrow the tool catalog and instructions to allow only tiktok_comment_by-url.

Risk: The skill uses DATAIFY_API_TOKEN for authenticated external Dataify API calls that may consume credits.

Mitigation: Keep the token in the environment, never expose it in chat or logs, and review target scope before high-volume or multi-page submissions.

## Reference(s):

- [Tool parameter catalog](references/tool-params.json)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-tiktok-comment-by-url)
- [Dataify builder endpoint](https://scraperapi.dataify.com/builder)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DATAIFY_API_TOKEN for authenticated Dataify requests; successful collections return final JSON results, with large payloads summarized while preserving raw result access.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
