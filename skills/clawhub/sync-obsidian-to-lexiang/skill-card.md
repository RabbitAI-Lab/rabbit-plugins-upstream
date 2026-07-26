## Description: <br>
Synchronizes an Obsidian vault one way to Tencent Lexiang, preserving folder structure while uploading Markdown pages and standalone attachments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajaxhe](https://clawhub.ai/user/ajaxhe) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Knowledge workers and developers use this skill to publish selected Obsidian vault content to a Lexiang knowledge base with dry-run previews, full or incremental sync, resume state, and conflict protection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads the selected Obsidian vault and uploads Markdown and attachments to Tencent Lexiang. <br>
Mitigation: Run with --dry-run first, restrict --source-dirs to intended content, and verify the target space and folder before a non-dry-run sync. <br>
Risk: The skill uses local Lexiang credentials and the security evidence notes an MCP proxy fallback that scans running agent processes for Authorization or session headers. <br>
Mitigation: Prefer explicit personal credentials with --lexiang-profile or --lexiang-credential-file, review or disable the MCP proxy fallback before installation, and avoid running it in shared sessions. <br>
Risk: The skill writes sync state inside the vault and can overwrite Lexiang pages during incremental sync. <br>
Mitigation: Use the default lexiang_wins conflict strategy unless Obsidian is the authoritative source, keep the manifest under backup, and review generated reports after sync. <br>


## Reference(s): <br>
- [Conflict Strategy](references/conflict-strategy.md) <br>
- [upload-markdown-to-lexiang](https://github.com/ajaxhe/upload-markdown-to-lexiang) <br>
- [Tencent Lexiang AI credential page](https://lexiangla.com/ai/claw) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Markdown, JSON, Files] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON sync summaries, local state files, and Markdown reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read a selected vault, upload Markdown and attachments to Tencent Lexiang, and write sync state under the vault plugin directory.] <br>

## Skill Version(s): <br>
2.1.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
