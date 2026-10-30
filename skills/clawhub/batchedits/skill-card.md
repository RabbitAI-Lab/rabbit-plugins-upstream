## Description:

Edit videos in bulk with BatchEdits - add captions, remove silences, crop to 9:16, zoom and cut long videos into clips with the BatchEdits CLI (or MCP server), then download the results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chuckwhisler](https://clawhub.ai/user/chuckwhisler)

### License/Terms of Use:

MIT-0

## Use Case:

External video creators and editors use this skill to process requested videos in batches, applying captions, silence removal, reframing, zoom, and clips through BatchEdits. It guides users through CLI or MCP setup and downloading completed edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video files are uploaded to BatchEdits for processing.

Mitigation: Confirm the selected files or folder and intended upload destination before processing.

Risk: Video processing and AI-selected clips may consume account credits.

Mitigation: Review the expected credit use with the user and obtain approval before starting processing.

Risk: A locally stored sign-in token or API key could expose the user's account if mishandled.

Mitigation: Keep credentials out of commands and chat, use the documented environment variable where applicable, and protect the local sign-in token.

## Reference(s):

- [BatchEdits CLI documentation](https://batchedits.com/docs/cli?utm_source=clawhub&utm_medium=skill)
- [BatchEdits MCP setup guide](https://batchedits.com/docs/mcp?utm_source=clawhub&utm_medium=skill)
- [BatchEdits on npm](https://www.npmjs.com/package/batchedits)
- [BatchEdits ChatGPT setup](https://batchedits.com/chatgpt?utm_source=clawhub&utm_medium=skill)
- [BatchEdits ClawHub release](https://clawhub.ai/chuckwhisler/skills/batchedits)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions]

**Output Format:** [Edited video files with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processed videos are downloaded to a user-selected location; processing may consume credits.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
