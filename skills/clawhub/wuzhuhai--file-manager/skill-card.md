## Description: <br>
File Manager helps an agent organize local files, batch rename files, find duplicate content, and preview or execute directory synchronization workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wuzhuhai](https://clawhub.ai/user/wuzhuhai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and power users can use this skill to plan and run file organization, duplicate cleanup, batch rename, and backup-style directory sync tasks. It is most appropriate when an agent should generate previews and guarded shell commands for local file-management workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports destructive or hard-to-reverse file operations, including delete actions, moves, renames, and mirror sync updates. <br>
Mitigation: Use it on a test folder first, require preview or dry-run output before execution, and keep backups before applying changes to important directories. <br>
Risk: Broad source or target paths can affect large portions of a home directory, cloud-synced folder, or backup tree. <br>
Mitigation: Constrain commands to specific project or staging directories and avoid broad paths unless the user has verified the preview and has a current backup. <br>
Risk: Mirror sync with deletion can remove target files that are not present in the source. <br>
Mitigation: Review the sync preview, avoid delete mode unless the target is disposable or backed up, and prefer quarantine or copy-based workflows where possible. <br>
Risk: Server-resolved source provenance is unavailable for this release. <br>
Mitigation: Treat the bundled files as the review boundary and do not infer GitHub provenance or upstream maintenance guarantees from skill text. <br>


## Reference(s): <br>
- [File Manager Skill Page](https://clawhub.ai/wuzhuhai/skills/file-manager) <br>
- [File Management Best Practices](artifact/references/best_practices.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and file-operation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preview-first workflows; execution may create, rename, move, copy, sync, or delete local files when users approve commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, created 2026-07-05T08:48:15Z) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
