## Description:

Turn public TikTok comments into one spoken reply clip per written line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, social operators, and agents use this skill to plan a TikTok comment reply voice pack and generate one reviewed spoken reply audio clip for each selected written reply.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags broad Beatra account authority, paid wallet operations, local credential storage, installation registration metadata, and automatic package updates.

Mitigation: Install only if the publisher is trusted, review before use, monitor Beatra charges and connected agents, and revoke the device in the Beatra Console when no longer needed.

Risk: Automatic updates are silent and enabled by default for the local package.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` when the installation should not check for or apply package updates automatically.

Risk: TikTok lookup, voice cloning, and speech synthesis can consume Beatra credits.

Mitigation: Use the documented six-field confirmation cards, live prices, unique request identities, and task polling before repeating any billable operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/tiktok-comment-reply-voice)
- [Beatra Skill Homepage](https://beatra.ai/skills/tiktok-comment-reply-voice)
- [TikTok Comment Reply Workflow](references/workflow.md)
- [Comment Lookup](references/comment-lookup.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [MCP Connection](references/mcp-connection.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)
- [Beatra MCP Endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell command examples; completed Beatra tasks can return MP3 audio artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires public TikTok comments or pasted comments, written reply lines, pronunciation guidance when names are present, clip count, voice choice, and explicit clone rights when voice cloning is requested.]

## Skill Version(s):

0.1.1 (source: server release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
