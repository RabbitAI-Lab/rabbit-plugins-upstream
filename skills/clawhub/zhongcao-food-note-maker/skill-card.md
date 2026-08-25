## Description:

Create a Xiaohongshu food post or REDnote food post from a dish photo, restaurant visit theme, or dining-atmosphere reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and marketing operators use this skill to plan and produce coordinated REDnote or Xiaohongshu food-post image sequences, titles, captions, and tags from a dish photo, restaurant visit concept, or dining-atmosphere reference. The skill can optionally perform paid Xiaohongshu lookup before drafting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared local Beatra credential with broad media and wallet-spend scopes.

Mitigation: Review the requested authorization before use and revoke the Beatra device authorization when the skill is no longer needed.

Risk: Source images may be uploaded to Beatra for generation or transformation.

Mitigation: Use only images the user is comfortable sending to Beatra and avoid private or sensitive media unless that transfer is acceptable.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when manual review of each package update is required.

Risk: Optional Xiaohongshu lookup and image generation can spend Beatra credits.

Mitigation: Require explicit confirmation of each paid lookup or generation request, including current price, maximum charge, and call count.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/zhongcao-food-note-maker)
- [Beatra skill homepage](https://beatra.ai/skills/zhongcao-food-note-maker)
- [Food-note planning](references/food-note-planning.md)
- [REDnote Food Note workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured paid-work confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit paid Beatra image generation or Xiaohongshu lookup requests only after explicit user confirmation.]

## Skill Version(s):

0.1.2 (source: server evidence release.version and artifact manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
