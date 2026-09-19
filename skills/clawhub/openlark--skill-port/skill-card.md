## Description:

Ports/adapts OpenClaw skills to other agent platforms (Claude Code, Codex, Cursor, Hermes, opencode, generic Agent Skills).

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlark](https://clawhub.ai/user/openlark)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to adapt OpenClaw skills for Claude Code, Codex, Cursor, Hermes, opencode, or generic Agent Skills platforms. It helps identify platform coupling, run deterministic replacements, and review remaining manual conversion work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The converter can copy files outside the selected skill folder through symlinks.

Mitigation: Run it only on trusted skill directories, inspect sources for symlinks first, and use a scratch output folder.

Risk: Generated ports may contain incomplete or incorrect handling for platform-specific features.

Mitigation: Review the dry-run output and the needs-manual-handling report before using or publishing generated ports.

Risk: Generated ports may include unintended local files if the source tree is not reviewed.

Mitigation: Inspect generated files before sharing or publishing them, and confirm that no unintended local files were copied.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/openlark/skills/skill-port)
- [Target Platform Quick Reference](references/platforms.md)
- [Tool Name & File & Path Mappings](references/tool-mappings.md)
- [OpenClaw-Specific Features and Handling Strategy](references/openclaw-specifics.md)
- [Example: Porting a Skill](references/example.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands, generated skill files, diffs, reports, and optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run mode is available for previewing conversions before writing ported skill files.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
