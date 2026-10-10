## Description:

Edit videos with BatchEdits by adding captions, removing silences, and applying saved styles, then check processing status and share download links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chuckwhisler](https://clawhub.ai/user/chuckwhisler)

### License/Terms of Use:

MIT-0

## Use Case:

People editing videos in their BatchEdits workspace use this skill to upload videos, select or create editing styles, queue processing with their approval, monitor progress, and obtain download links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded videos and the workspace API key are shared with BatchEdits.

Mitigation: Confirm that BatchEdits is trusted with the videos and key; keep the key in the environment, not in chats or URLs.

Risk: Processing videos consumes video credits.

Mitigation: Confirm each processing request and the number of credits for bulk jobs before queuing.

## Reference(s):

- [BatchEdits on ClawHub](https://clawhub.ai/chuckwhisler/skills/batchedits)
- [BatchEdits MCP setup guide](https://batchedits.com/mcp/docs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with status updates and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shares temporary download links only for completed videos; processing requires user confirmation.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
