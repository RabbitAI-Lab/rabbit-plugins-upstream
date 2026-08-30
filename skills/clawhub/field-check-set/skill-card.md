## Description:

Turn user-supplied on-site inspection check item names and check points into a four-to-eight still field check set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field teams and their supporting agents use this skill to turn approved inspection item names and check points into a consistent four-to-eight still image pack. The skill also guides planning, approval, billing recovery, task polling, and review of returned Beatra image-generation artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device credential and can perform wallet-backed paid operations.

Mitigation: Install only where broad Beatra account access and paid generation are acceptable, and require explicit user approval before each billable generation request.

Risk: The bundled client can silently update package files after installation.

Mitigation: Review the package before installation and disable automatic updates with scripts/mcp_client.py update --auto off when a pinned local package is required.

Risk: Transport uncertainty or changed generation arguments could lead to duplicate or unintended paid tasks.

Mitigation: Use one opaque client_request_id per approved still, retry only byte-identical uncertain requests, and mint a new request ID for changed work.

Risk: Generated inspection stills could be mistaken for official findings or compliance guarantees.

Mitigation: Use only user-supplied check items and check points, omit unsupported conclusions, and review visible printed text before delivery.

## Reference(s):

- [Field check pack workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/field-check-set)
- [Beatra skill homepage](https://beatra.ai/skills/field-check-set)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with JSON and shell command snippets; generated still image artifacts are returned through Beatra tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one still per supplied check item, normally four to eight stills, with one billable generation request per still.]

## Skill Version(s):

0.1.1 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
