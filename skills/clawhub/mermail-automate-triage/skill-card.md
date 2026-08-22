## Description:

Create, inspect, update, and delete Mermail task triagers and review recent triager runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to create, debug, update, or delete Mermail mailbox triage automations while reviewing mailbox scope, recent run status, safety limits, and intended effects before changes are applied.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Triage automation changes can broaden mailbox scope, sender scope, outputs, or external effects beyond what the user intended.

Mitigation: Review the exact configuration diff, sender scope, volume limits, output settings, and allowlists before approving any create or update operation.

Risk: Inbound email content can contain untrusted instructions, links, attachments, credentials, OTPs, or magic links.

Mitigation: Require clean scan status, sanitized bounded content, isolated verification mailboxes, and fresh human confirmation before sends, deletion, external disclosure, credentials, account changes, OTP use, or financial effects.

Risk: Deleting a triager is destructive and may remove an automation configuration that still needs diagnosis.

Mitigation: Require explicit approval for the exact triager and arguments, use the prepared destructive-action token once, and verify final state with a follow-up read.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP endpoint](https://console.mermail.app/mcp)
- [Triager security boundary](references/security.md)
- [Triage tool map](references/tools.md)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with structured triager inventories, debugging reports, configuration proposals, diffs, and final-state summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Mermail API key and live Mermail workspace context.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
