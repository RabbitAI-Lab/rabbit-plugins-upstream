## Description:

Create a vertical WeChat Channels product-display video from a real product photo and confirmed product information. Shape a clear product opening, one detail or use moment, and a clean ending, then prepare the finished product video with a title and publishing copy for WeChat Channels product content, including a new-product showcase video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and operator agents use this skill to turn a real product photo and confirmed product facts into a vertical WeChat Channels showcase video, title, and publishing copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release uses a shared local bearer token and broad Beatra account scopes, including spending authority.

Mitigation: Authorize only in an environment where paid Beatra video generation and local product-photo upload are intended, protect the local credential, and disconnect through the documented uninstall flow when no longer needed.

Risk: The workflow can submit paid image and video generation tasks.

Mitigation: Require the documented admission card and explicit user confirmation before each paid stage, then reuse the same request identity for recovery instead of creating replacement paid work.

Risk: The bundled client silently updates package-owned files by default.

Mitigation: Review the automatic update behavior before installation and disable silent checks with the documented update command when that posture is not acceptable.

## Reference(s):

- [WeChat Channels Product Showcase Video Maker](https://clawhub.ai/beatra-ai/skills/wechat-channels-product-video)
- [Video Channels product-display planning](artifact/references/video-channel-planning.md)
- [WeChat Channels product-display video workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Markdown, Text]

**Output Format:** [Markdown with structured task facts, artifact URLs or IDs, title, caption, and inline shell commands when setup or recovery is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include billable Beatra task status, returned media properties, usage, and net charged credits after terminal completion.]

## Skill Version(s):

0.1.5 (source: evidence.release.version and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
