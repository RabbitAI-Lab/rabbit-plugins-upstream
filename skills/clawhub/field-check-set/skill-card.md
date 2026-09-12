## Description:

Turn user-supplied on-site inspection check item names and check points into a four-to-eight still field check set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and field teams use this skill to plan and generate matching field-check still image packs from supplied inspection item names and approved check points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests a shared Beatra bearer credential with powers broader than still-image generation.

Mitigation: Install only if those account powers are acceptable, and prefer a dedicated Beatra account or low-balance wallet for this workflow.

Risk: Silent automatic updates are enabled by default.

Mitigation: Disable automatic updates with scripts/mcp_client.py update --auto off when you need review before replacement.

Risk: A retained device credential can continue to access Beatra until revoked or expired.

Mitigation: Revoke the connected device from the Beatra Console when finished, especially on shared or temporary machines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/field-check-set)
- [Beatra skill homepage](https://beatra.ai/skills/field-check-set)
- [Field check pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with JSON payloads, shell commands, and generated image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one still per named check item, usually four to eight stills, and reports returned task, model, artifact, and billing fields.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
