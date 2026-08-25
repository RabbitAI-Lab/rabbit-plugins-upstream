## Description:

Create Xiaohongshu beauty and skincare content from product facts, routine steps, skin concerns, and audience context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and beauty operators use this skill to turn supplied beauty or skincare facts into a Xiaohongshu note pack with titles, review copy, a four-slide 3:4 plan, cover text, hashtags, and a comment starter. The workflow screens claims for unsupported beauty, efficacy, medical, ranking, and conversion language before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra Device Token and can connect the agent to Beatra account capabilities beyond beauty-note planning.

Mitigation: Install only for users who trust Beatra with that account authority, keep the token out of chat and logs, and revoke or uninstall the connection when it is no longer needed.

Risk: The bundled client can upload local files and call generic Beatra tools when invoked.

Mitigation: Review each requested Beatra action before execution and avoid sending sensitive local files unless the user explicitly intends that upload.

Risk: Automatic updates are silent by default and can replace package-owned files.

Mitigation: Use the documented update controls to turn automatic updates off or check available updates before accepting replacement.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/beatra-ai/skills/rednote-beauty-note-maker)
- [Beatra Skill Homepage](https://beatra.ai/skills/rednote-beauty-note-maker)
- [Beauty note workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured note sections and inline shell commands when setup or diagnostics are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces text and layout planning in the current conversation; it does not create a paid generation task.]

## Skill Version(s):

0.1.1 (source: evidence.release.version and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
