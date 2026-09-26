## Description: <br>
Helps agents manage Baidu Netdisk files under `/apps/bdpan/` through the `bdpan` CLI, including upload, download, transfer, sharing, search, and agent-memory backup or restore. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate Baidu Netdisk files in the scoped `/apps/bdpan/` area, including file lifecycle actions, share-link handling, large-download workflow guidance, and selected agent-memory backup or restore tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad control over Baidu Netdisk files, including sharing, moves, uploads, deletes, overwrites, and restores. <br>
Mitigation: Use only when that level of account access is intended, keep operations scoped to `/apps/bdpan/`, and require explicit confirmation before sharing, moving, uploading, deleting, overwriting, or restoring files. <br>
Risk: Agent-memory backup and restore may handle sensitive local memory files or overwrite existing memory. <br>
Mitigation: Avoid memory backup or restore when agent memory may contain secrets, inspect restore sources before use, and confirm the overwrite set before restoring. <br>
Risk: Large downloads may continue as detached background jobs after the agent session ends. <br>
Mitigation: Monitor background PIDs and logs during large downloads, and clean up unfinished jobs manually if the session ends. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/baidu-netdisk-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command-output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run `bdpan` CLI operations, report progress for background downloads, and summarize file-operation results.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists 1.1.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
