## Description:

TinkerClaw WhatsApp helps OpenClaw agents use WhatsApp actions and multi-agent group protocols, and includes opt-in scripts for contact inventory, group creation, and OpenClaw source patches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators using TinkerClaw or OpenClaw use this skill to guide WhatsApp messaging, group workflows, multi-agent conversation controls, and optional maintenance tasks. It is intended for installations where the operator controls the WhatsApp account and can review privacy-impacting actions before running scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional scripts can use WhatsApp session credentials and act through the operator's WhatsApp account.

Mitigation: Read each script before execution and run only after confirming the disclosed action; scripts refuse to proceed without --yes.

Risk: Contact enumeration can expose group membership and phone numbers, especially when --resolve-lids or --save is used.

Mitigation: Use the default masked, in-memory mode where possible; use --resolve-lids or --save only when necessary and delete saved exports when finished.

Risk: The history patch can enable broad, indefinite local storage of inbound WhatsApp messages.

Mitigation: Avoid applying the history-retention patch unless there is a clear need and consent or notice basis; use --revert and remove retained data when it is no longer needed.

Risk: The source-patching scripts edit an OpenClaw checkout in place.

Mitigation: Review the target checkout before applying patches, keep the generated backups, and use --revert if the change is not desired.

Risk: Documented npx script execution can depend on an unpinned runtime resolution.

Mitigation: Run from a locally locked OpenClaw checkout or pin the runtime before using the npx commands.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/globalcaos/skills/whatsapp-ultimate)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [TinkerClaw project reference](https://github.com/globalcaos/tinkerclaw)
- [OpenClaw project](https://github.com/openclaw/openclaw)
- [Baileys library](https://github.com/WhiskeySockets/Baileys)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with command and configuration snippets; bundled scripts may emit terminal output or JSON when explicitly run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional scripts are consent-gated with --yes; contact export is off by default and saved files are documented as mode 0600.]

## Skill Version(s):

4.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
