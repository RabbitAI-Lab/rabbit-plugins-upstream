## Description:

Create Xiaohongshu or REDnote copy from a product, experience, topic, or audience brief. This AI Xiaohongshu copywriter produces title options, a structured note body, cover wording, relevant hashtags, and a natural comment starter for product discovery, local experiences, beauty, food, fashion, travel, and knowledge posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to draft editable Xiaohongshu or REDnote post copy from a supplied product, experience, topic, or audience brief. It produces text-first note assets and flags assumptions or unsupported claims before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package can authorize a broad Beatra account token and store shared local state for Beatra access.

Mitigation: Install only if that account-level access is acceptable; keep the Beatra credential files private and use the bundled uninstall flow or Beatra Console revocation when access is no longer needed.

Risk: The bundled client can upload selected local files and call arbitrary Beatra MCP tools.

Mitigation: Review each tool call and stdin JSON before execution, and upload only files the user explicitly selected for the Beatra workflow.

Risk: Silent automatic updates can replace package-owned executable files without a separate confirmation step.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` when manual change control is required; otherwise rely on the documented checksum-verified update path.

Risk: Generated marketing copy can include unsupported claims, absolute superlatives, or regulated efficacy language.

Mitigation: Confirm factual claims with the user and apply the workflow copy screen before publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/rednote-note-copywriter)
- [Beatra skill homepage](https://beatra.ai/skills/rednote-note-copywriter)
- [REDnote note copy workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown text with title options, a primary title, note body, cover phrases, hashtags, a comment starter, assumptions, and missing facts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Non-billable text planning; it does not create images, publish to REDnote, or create a paid generation task.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
