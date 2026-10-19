## Description:

Helps agents edit videos in bulk with captions, silence removal, vertical crops, zooms, and clips through BatchEdits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chuckwhisler](https://clawhub.ai/user/chuckwhisler)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to apply consistent edits to batches of videos and download the results through the BatchEdits CLI or connected chat tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned npm CLI can execute code that has not been reviewed for this release.

Mitigation: Use a pinned or preinstalled, reviewed BatchEdits CLI version and install only if you trust the publisher.

Risk: Processing local videos with BatchEdits authentication may expose unintended files or credentials.

Mitigation: Restrict runs to the intended video folder and keep API keys out of chat and command lines.

Risk: Bulk processing consumes BatchEdits credits.

Mitigation: Confirm expected credit use with the user before processing.

## Reference(s):

- [BatchEdits ClawHub release](https://clawhub.ai/chuckwhisler/skills/batchedits)
- [BatchEdits CLI documentation](https://batchedits.com/docs/cli?utm_source=clawhub&utm_medium=skill)
- [BatchEdits MCP setup guide](https://batchedits.com/docs/mcp?utm_source=clawhub&utm_medium=skill)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and CLI JSON status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Edited videos are downloaded to a user-selected folder; processing consumes credits.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
