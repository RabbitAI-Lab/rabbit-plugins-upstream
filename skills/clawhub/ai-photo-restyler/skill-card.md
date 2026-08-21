## Description:

AI Photo Restyler helps an agent redraw an existing photo into anime, manga, comic, cartoon, watercolor, clay, or 3D character art while keeping the subject recognizable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill through an agent to restyle portraits, pets, products, travel photos, and content batches into a selected illustration style while preserving key subject features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for a shared Beatra device token with broad Beatra capabilities, not only photo editing.

Mitigation: Review the requested Beatra access before installation, keep the token only in the local credentials file, and reconnect only when the user explicitly chooses to do so.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` when tighter change control is needed, and rely on the documented update verification checks before accepting replacement files.

Risk: Photo restyling creates paid asynchronous generation tasks, so retries or changed inputs can create additional charges.

Mitigation: Confirm the frozen prompt, ordered inputs, model, canvas, output count, maximum charge, and client request ID before submission; reuse the same request identity only for byte-equivalent recovery.

## Reference(s):

- [Photo restyle workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/ai-photo-restyler)
- [Beatra skill homepage](https://beatra.ai/skills/ai-photo-restyler)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides paid asynchronous Beatra image generation; requires confirmation before paid work and reports returned task, artifact, model, dimensions, format, and billing fields.]

## Skill Version(s):

0.1.3 (source: server evidence release.version and artifact manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
