## Description:

Polish an existing AI video with a focused realism pass for more natural light, materials, color balance, and less distracting repeated detail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to prepare one existing AI-generated short video for a Beatra video-edit task that retouches one realism issue while preserving accepted subject, framing, timing, and mood.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for a broad Beatra device authorization that can spend credits and access multiple media capabilities.

Mitigation: Install only if this authorization is acceptable, confirm the final paid payload before submission, and revoke the Beatra device authorization when finished.

Risk: Selected videos are uploaded to the Beatra service for retouching.

Mitigation: Use only clips approved for upload and avoid sending sensitive or unauthorized media.

Risk: Default silent package updates can replace local package code.

Mitigation: Review the automatic update behavior and disable silent checks with the documented update command when pinned local code is required.

Risk: Transport uncertainty or retries could otherwise create duplicate paid work.

Mitigation: Preserve the same client request identity for recovery and check existing tasks before replaying a paid request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/video-realism-retoucher)
- [Beatra skill homepage](https://beatra.ai/skills/video-realism-retoucher)
- [Focused video realism retouch workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [MCP connection](references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single source-led retouch workflow; paid requests require user confirmation and task polling.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
