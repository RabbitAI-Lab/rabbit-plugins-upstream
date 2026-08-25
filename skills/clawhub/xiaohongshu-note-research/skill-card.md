## Description:

Turns a Xiaohongshu category, note link, or pasted notes into a research memo with title patterns, structure, verbatim comments, and followable angles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams use this skill to study Xiaohongshu notes they paste or optionally look up, then receive a research memo that preserves observed title patterns, structure, comments, and followable content angles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device authorization stored on disk with broader account capabilities than the note memo itself needs.

Mitigation: Install only when that authorization model is acceptable, keep the local credential private, and use the bundled uninstall and disconnect workflow when removing the package.

Risk: The bundled client can silently update installed package files.

Mitigation: Review the automatic update behavior before installing and disable silent checks with scripts/mcp_client.py update --auto off when manual update control is required.

Risk: Optional Xiaohongshu lookups are paid and repeated pages or changed arguments can create additional charges.

Mitigation: Confirm each lookup separately, quote the live price before execution, and preserve the same client_request_id only for byte-identical recovery of an uncertain request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/xiaohongshu-note-research)
- [Beatra skill homepage](https://beatra.ai/skills/xiaohongshu-note-research)
- [Looking up notes](references/note-lookup.md)
- [Writing the research memo](references/research-memo.md)
- [Note research workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research memo with optional command snippets and JSON task or billing facts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When a paid lookup runs, the skill reports the returned payload, task ID, terminal status, and billing.net_charged_credits.]

## Skill Version(s):

0.1.1 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
