## Description: <br>
Clawd Modifier helps users customize the Claude Code mascot by changing colors, adding arms or accessories, applying ASCII art variants, extracting the current mascot state, and restoring the original appearance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[masonc15](https://clawhub.ai/user/masonc15) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Claude Code users use this skill to personalize the Claude Code terminal mascot with scripted color and ASCII art changes, inspect the current mascot state, and recover the original appearance when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can rewrite installed Claude Code JavaScript or binary files, which may break the CLI or conflict with updates and integrity checks. <br>
Mitigation: Use dry-run modes first, pass explicit target paths, keep backups, and test Claude Code after changes. <br>
Risk: Binary patching is fragile across Claude Code versions and may not match expected byte patterns. <br>
Mitigation: Prefer the cli.js color and art patchers when possible, and use the binary patcher only after creating a backup and confirming the restore path. <br>
Risk: Skipping backups or making manual edits can remove the quickest recovery path. <br>
Mitigation: Avoid no-backup modes unless an external backup exists, and use the restore flags or saved backup files after an unsuccessful change. <br>


## Reference(s): <br>
- [Clawd Anatomy](references/clawd-anatomy.md) <br>
- [Unicode Block Drawing Characters](references/unicode-blocks.md) <br>
- [Clawd Variant Gallery](assets/clawd-variants.txt) <br>
- [ClawHub Skill Page](https://clawhub.ai/masonc15/skills/clawd-modifier) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and Python script usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may direct scripts to rewrite installed Claude Code files; dry-run, backup, restore, and explicit target-path options are available in the artifact scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and user changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
