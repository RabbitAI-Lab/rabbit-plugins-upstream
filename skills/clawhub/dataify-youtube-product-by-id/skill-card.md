## Description:

Collects structured YouTube video metadata by video ID through Dataify, including title, channel, counts, and details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify collection jobs for YouTube video basic information by video ID, monitor completion, and return final JSON results when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a saved Dataify API TOKEN and sends YouTube video IDs plus selected collection options to Dataify.

Mitigation: Confirm the user is authorized to use the configured Dataify account, verify only whether DATAIFY_API_TOKEN is present, and never print or silently persist the token.

Risk: The security summary notes that runtime behavior supports broader collection than the one-video description promises, including multiple video IDs.

Mitigation: Confirm scope and likely credit usage before high-volume or multi-input runs, and make clear when multiple video IDs will be submitted.

Risk: The skill may wait for asynchronous task completion and download final results after submitting a paid collection task.

Mitigation: On timeout or interruption, return the task ID and a resume path rather than resubmitting the same paid task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-product-by-id)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell commands and JSON task or result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May wait for asynchronous Dataify task completion and return a summarized final JSON result while preserving access to the raw result.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
