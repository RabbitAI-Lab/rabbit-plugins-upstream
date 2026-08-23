## Description:

Create Xiaohongshu or REDnote copy from a product, experience, topic, or audience brief. This AI Xiaohongshu copywriter produces title options, a structured note body, cover wording, relevant hashtags, and a natural comment starter for product discovery, local experiences, beauty, food, fashion, travel, and knowledge posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and agents use this skill to turn supplied product, experience, topic, or audience facts into editable Xiaohongshu or REDnote note copy. It drafts title options, a primary note body, cover wording, hashtags, a comment starter, and clearly marked assumptions or missing facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags account authorization, upload, credential, and silent update powers as broader than expected for a text-copywriting workflow.

Mitigation: Review the package before use, proceed only if broad Beatra device credential access is acceptable, and prefer or request a version without bundled auth, upload, and auto-update behavior when those powers are unnecessary.

Risk: Automatic updates are enabled silently by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` before use when change control or review is required.

Risk: Generated marketing copy could include unsupported claims, absolute superlatives, regulated-category efficacy claims, or outcome promises.

Mitigation: Use the bundled workflow screen before publication and replace or confirm unsupported claims instead of adding disclaimers.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/rednote-note-copywriter)
- [Beatra package homepage](https://beatra.ai/skills/rednote-note-copywriter)
- [REDnote note copy workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured copy sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces five title options, one primary note body, three cover phrases, five to ten hashtags, one comment starter, assumptions, and missing facts.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
