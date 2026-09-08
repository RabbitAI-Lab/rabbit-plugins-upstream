## Description:

TinkerClaw WhatsApp helps agents use OpenClaw's WhatsApp channel for multi-agent group coordination, supported WhatsApp actions, and opt-in maintenance scripts for contact inventory, group creation, history capture, and response prefixing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators using TinkerClaw or OpenClaw use this skill to configure multi-agent WhatsApp discussions, reference WhatsApp channel actions, and run explicit opt-in scripts for WhatsApp contacts, groups, local history capture, and reply prefix behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled scripts can read WhatsApp linked-device credentials and connect to WhatsApp as the user's account.

Mitigation: Run only after reviewing the script behavior and use the documented --yes consent gate with a known WA_AUTH_DIR.

Risk: Contact inventory and LID resolution can expose information about group members who have not consented.

Mitigation: Keep the default masked, in-memory behavior; avoid --resolve-lids and --save unless there is a specific need, and delete any saved export when finished.

Risk: The history patch can enable indefinite local retention of inbound WhatsApp messages.

Mitigation: Apply the patch only when message retention is required, disclose or obtain consent where applicable, and use --revert plus database deletion when retention is no longer needed.

Risk: Group creation and group management actions are visible to real WhatsApp participants and may not be silently reversible.

Mitigation: Require explicit human confirmation before creating groups, changing membership or admin status, unsending messages, or handling invite links.

Risk: Source-patching scripts and npx tsx execution create local code-execution and mutable dependency exposure.

Mitigation: Review and harden OPENCLAW_SRC handling, run from a trusted OpenClaw checkout with expected dependencies, and use the backup and --revert path for rollback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/whatsapp-ultimate)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [TinkerClaw project](https://github.com/globalcaos/tinkerclaw)
- [OpenClaw](https://github.com/openclaw/openclaw)
- [Baileys](https://github.com/WhiskeySockets/Baileys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples, configuration snippets, and bundled TypeScript and Bash scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bundled scripts are documented as explicit opt-in actions and refuse to run without --yes.]

## Skill Version(s):

4.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
