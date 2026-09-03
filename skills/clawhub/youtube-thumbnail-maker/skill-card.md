## Description:

Creates YouTube thumbnail directions from a topic, title, script, key frame, portrait, product photo, or channel reference, then renders the chosen 16:9 image through Beatra with title-matching and channel consistency guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, channel teams, and agents use this skill to plan three structurally distinct long-form YouTube thumbnail directions, align the selected direction with the video title, and render or refine a 16:9 thumbnail through a connected Beatra account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses a broad local Beatra Device Token for the connected account.

Mitigation: Install only when the user accepts that connection; keep the credential private, use the bundled authorization flow, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The bundled client can check for and install package updates automatically by default.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` after installation when manual review is preferred before updates.

Risk: Rendering with supplied frames, portraits, product photos, or channel references uploads selected source images to Beatra.

Mitigation: Use only source images the user intends to send to Beatra, and confirm the source and reference order before paid rendering.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/youtube-thumbnail-maker)
- [Beatra skill homepage](https://beatra.ai/skills/youtube-thumbnail-maker)
- [YouTube thumbnail workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, image artifacts, guidance]

**Output Format:** [Markdown guidance with shell commands and Beatra task results; generated thumbnail artifacts are returned as links with dimensions, format, resolved model, task ID, and billing facts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected Beatra account and explicit approval before paid rendering; selected source images may be uploaded to Beatra.]

## Skill Version(s):

0.2.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
