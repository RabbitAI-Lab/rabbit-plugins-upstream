## Description: <br>
Obsidian vault automation for configured vaults such as `obsidian-2026`: vault status/doctor, host Git sync/status with Obsidian Git plugin fallback only when host `git` is not found, Tasks todos, journal records, file or attachment records, project files under `01_project/` (`创建项目`, `项目记录`, `记到某项目`, `补充功能需求/非功能需求/决策/任务/问题`), QuickAdd, Journals, plugin/native commands, safe vault read/search, and OpenClaw sync. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dxshelley](https://clawhub.ai/user/dxshelley) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate configured Obsidian vaults through repeatable workflows for status checks, Git-backed synchronization, task and journal updates, project records, attachments, safe vault reads/searches, plugin commands, and OpenClaw synchronization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can edit a configured Obsidian vault and normal workflows may commit and push vault changes or copied attachments. <br>
Mitigation: Install only for vaults where agent edits and Git sync are intended; review the target vault and remote repository first, and use local-only modes when remote sync is not desired. <br>
Risk: Broad vault access can expose personal or sensitive note content if reads and searches are not scoped. <br>
Mitigation: Use the documented safe-read and safe-search workflows, avoid arbitrary outside-vault reads, and redact sensitive content before returning note excerpts. <br>
Risk: Attachment-backed records can copy local files into the vault. <br>
Mitigation: Require readable, explicitly supplied attachment paths or staged attachment selectors, and stop instead of creating partial records when attachment paths are unavailable. <br>
Risk: Git conflicts, unmerged states, or unfinished merges can corrupt expected sync behavior. <br>
Mitigation: Run vault doctor and Git status checks before writes or sync, and stop on nonzero results, unmerged files, merge state, or unresolved workflow reasons. <br>


## Reference(s): <br>
- [User usage examples](docs/user-usage.md) <br>
- [Agent usage examples](docs/agent-usage-examples.md) <br>
- [Fast paths](references/fast-paths.md) <br>
- [Runtime sync](references/runtime-sync.md) <br>
- [Vault safety](references/vault-safety.md) <br>
- [Task add](references/task-add.md) <br>
- [Task query](references/task-query.md) <br>
- [Record workflows](references/record-workflows.md) <br>
- [Record body](references/record-body.md) <br>
- [Official CLI](references/official-cli.md) <br>
- [OpenClaw compatibility](references/openclaw.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-producing workflow expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may create or update Obsidian Markdown notes, copy attachments, and perform Git sync when the selected workflow calls for it.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
