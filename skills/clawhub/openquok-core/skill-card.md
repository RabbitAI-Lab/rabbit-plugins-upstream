## Description:

Schedule and manage social posts with the openquok CLI: authenticate, upload media, create drafts and scheduled posts, configure internal plugs, and read channel analytics for integrations in an OpenQuok workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratimon](https://clawhub.ai/user/ratimon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, social media operators, and agent users use this skill to schedule, draft, reschedule, and monitor social posts across connected OpenQuok integrations through the openquok CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is always enabled and may run OpenQuok CLI version and authentication checks at session start.

Mitigation: Deploy it only where an always-available OpenQuok assistant is expected, and review the startup authentication-check behavior before installation.

Risk: Authenticated commands can act on connected social accounts and workspace content.

Mitigation: Use least-privilege workspace access, confirm integration UUIDs before posting, and avoid exposing programmatic tokens in chat or logs.

Risk: Plug automation can create cross-account comments, reposts, or reshares after publish.

Mitigation: Review plug settings and acting integration IDs before creating or activating plugs, especially for cross-account workflows.

Risk: Draft, inbox, private, and direct-publish settings can affect where TikTok content appears.

Mitigation: Confirm TikTok privacy level and content posting method with the user before scheduling or publishing.

## Reference(s):

- [OpenQuok CLI package](https://www.npmjs.com/package/@openquok/auto-cli)
- [OpenQuok website](https://www.openquok.com/)
- [ClawHub skill page](https://clawhub.ai/ratimon/skills/openquok-core)
- [OpenQuok CLI command reference](artifact/resources/command-reference.md)
- [Provider settings reference](artifact/resources/provider-settings.md)
- [Workflow recipes](artifact/resources/patterns.md)
- [Plugs reference](artifact/resources/plugs.md)
- [JSON post examples](artifact/resources/examples/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline openquok CLI commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the openquok CLI on PATH and valid OpenQuok workspace credentials for API-backed actions.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
