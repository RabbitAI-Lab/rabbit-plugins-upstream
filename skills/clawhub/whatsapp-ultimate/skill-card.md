## Description:

TinkerClaw WhatsApp documents OpenClaw/TinkerClaw WhatsApp channel actions and Protocol v2 controls for multi-agent WhatsApp groups, including congestion control, conversation lifecycle, budget-aware scheduling, and safety notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill as a reference for enabling WhatsApp messaging, media, interaction, group-management, local-history search, and multi-agent discussion behavior through an existing OpenClaw/TinkerClaw WhatsApp channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced WhatsApp channel can perform real-world messaging and group actions, including sending messages, deleting messages, changing group membership, and changing admin status.

Mitigation: Keep human confirmation enabled for destructive or public-facing WhatsApp actions, especially unsend, participant removal, admin changes, and group leave actions.

Risk: Group invite links can allow anyone with the link to join and should be treated as sensitive access material.

Mitigation: Avoid posting invite links into logs or unrelated chats, and revoke links when they may have been exposed.

Risk: Local WhatsApp history search depends on messages captured while the channel was running and may miss periods when the gateway was down.

Mitigation: Verify channel history retention settings and treat empty search results as possibly incomplete rather than authoritative.

Risk: Bulk or rapid WhatsApp messaging can trigger anti-spam controls or unwanted contact with users.

Mitigation: Avoid bulk messaging, rapid-fire sends, and unsolicited messages to contacts who have not opted in or previously messaged the account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/whatsapp-ultimate)
- [TinkerClaw repository](https://github.com/globalcaos/tinkerclaw)
- [OpenClaw repository](https://github.com/openclaw/openclaw)
- [Baileys repository](https://github.com/WhiskeySockets/Baileys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown documentation with WhatsApp action examples and YAML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only release; the package itself ships no scripts, installers, background processes, or telemetry.]

## Skill Version(s):

4.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
