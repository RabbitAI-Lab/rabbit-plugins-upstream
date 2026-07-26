## Description: <br>
Schedule and manage social posts with the openquok CLI: authenticate, upload media, create drafts and scheduled posts, configure internal plugs, and read channel analytics for integrations in an OpenQuok workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ratimon](https://clawhub.ai/user/ratimon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and social media teams use this skill to guide an agent through OpenQuok CLI workflows for authenticated social channel management, scheduled publishing, media upload, provider settings, analytics, and post-publish engagement automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to OpenQuok credentials and connected social accounts. <br>
Mitigation: Install only when the user trusts OpenQuok with those accounts and use the documented OAuth or programmatic-token flows. <br>
Risk: Posting, deletion, status changes, and plug activation can affect live social channels. <br>
Mitigation: Review post content, integration IDs, schedule times, privacy settings, provider settings, and plug rules before running create, delete, status, or activation commands. <br>
Risk: Media uploads and public HTTPS media fetches may expose confidential files. <br>
Mitigation: Avoid confidential media, upload through OpenQuok first, and verify returned media identifiers and paths before using them in post payloads. <br>
Risk: Engagement automation can generate replies, comments, reposts, or reshares after publishing. <br>
Mitigation: Use plug rules only after reviewing the target channels, thresholds, acting integration IDs, messages, and platform policy implications. <br>


## Reference(s): <br>
- [OpenQuok Core on ClawHub](https://clawhub.ai/ratimon/skills/openquok-core) <br>
- [OpenQuok CLI package](https://www.npmjs.com/package/@openquok/auto-cli) <br>
- [Command reference](artifact/resources/command-reference.md) <br>
- [Provider settings](artifact/resources/provider-settings.md) <br>
- [Plugs reference](artifact/resources/plugs.md) <br>
- [Example payload index](artifact/resources/examples/EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the openquok CLI on PATH and valid OpenQuok credentials before API-backed commands can run.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
