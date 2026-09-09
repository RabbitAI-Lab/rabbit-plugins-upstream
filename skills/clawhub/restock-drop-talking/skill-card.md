## Description:

Turn seller-supplied restock facts and an already-written restock script into one talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and their agents use this skill to plan, authorize, and produce short restock announcement talking clips from seller-supplied stills, restock facts, and spoken lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package stores a broad Beatra device token with paid-generation and wallet-spend authority.

Mitigation: Install only when that authority is acceptable, keep the token confined to local Beatra state, and use a dedicated Beatra account or credential scope if available.

Risk: The bundled client silently self-updates executable package code by default.

Mitigation: Review the package before installation and disable automatic updates with scripts/mcp_client.py update --auto off when change control is required.

Risk: Paid clone, speech, and video stages can create charges or duplicate work if retried incorrectly.

Mitigation: Require explicit approval for each paid stage and reuse the same client_request_id only for byte-identical recovery retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/restock-drop-talking)
- [Beatra skill homepage](https://beatra.ai/skills/restock-drop-talking)
- [Restock talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON payloads and shell commands; generated media is returned as separate Beatra task output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 2 to 8 clips by default and requires separate approval for paid clone, speech, and video stages.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
