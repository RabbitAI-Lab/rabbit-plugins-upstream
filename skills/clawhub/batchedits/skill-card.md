## Description:

Edit videos in bulk with BatchEdits - add captions, remove silences, crop to 9:16, zoom and cut long videos into clips with the BatchEdits CLI (or MCP server), then download the results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chuckwhisler](https://clawhub.ai/user/chuckwhisler)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to prepare batches of videos with captions, silence removal, reframing, zooms, and clips. It guides an agent through configuring BatchEdits and returning the processed videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One local reference could not be resolved, leaving the scan incomplete at medium confidence.

Mitigation: Review the unresolved reference and the skill instructions before installing if greater assurance is needed.

Risk: The CLI or MCP setup uses a BatchEdits API credential.

Mitigation: Keep BATCHEDITS_API_KEY in the environment or approved secret storage; do not put it in commands, URLs, or chat messages.

## Reference(s):

- [BatchEdits CLI documentation](https://batchedits.com/docs/cli?utm_source=clawhub&utm_medium=skill)
- [BatchEdits MCP documentation](https://batchedits.com/docs/mcp?utm_source=clawhub&utm_medium=skill)
- [BatchEdits npm package](https://www.npmjs.com/package/batchedits)
- [BatchEdits ClawHub release](https://clawhub.ai/chuckwhisler/skills/batchedits)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Video files]

**Output Format:** [Markdown guidance with inline shell commands and configuration instructions; processed video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video edits and options follow the user's requested style and processing choices.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
