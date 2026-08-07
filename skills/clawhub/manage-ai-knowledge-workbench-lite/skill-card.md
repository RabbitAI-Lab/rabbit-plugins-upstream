## Description: <br>
AI Knowledge Workbench Lite builds and refreshes a metadata-only local knowledge index and offline HTML dashboard for a user-authorized Markdown folder or Obsidian vault. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexfengrui](https://clawhub.ai/user/alexfengrui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge workers, and agent users use this skill to turn one authorized local Markdown folder or Obsidian vault into a metadata-only derived knowledge index and offline dashboard, then refresh, inspect, or safely uninstall the managed state on demand. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated local indexes, dashboard files, and diagnostics can expose metadata such as relative paths, tags, headings, links, hashes, and environment details. <br>
Mitigation: Use the skill only with workspaces or vaults suitable for local indexing, and review generated files or diagnostic output before sharing them. <br>
Risk: The runtime reads authorized Markdown to extract metadata, so using it on an unintended directory could expose local structure to generated outputs. <br>
Mitigation: Run it only against one user-authorized workspace or source directory, and pause for confirmation before accessing new directories, deleting outputs, or performing external data transfer. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/alexfengrui/skills/manage-ai-knowledge-workbench-lite) <br>
- [Lite runtime contract](references/RUNTIME_CONTRACT.md) <br>
- [Lite privacy boundary](references/PRIVACY.md) <br>
- [Lite autonomy and gates](references/AUTONOMY_GATES.md) <br>
- [OpenClaw Getting Started](https://docs.openclaw.ai/start/getting-started) <br>
- [Python downloads](https://www.python.org/downloads/) <br>
- [Obsidian downloads](https://obsidian.md/download) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown or text guidance with structured JSON command status; generated workspace files include derived Markdown indexes and an offline HTML dashboard.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Metadata-only local processing; writes reserved derived directories only inside the selected workspace.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata, SKILL.md frontmatter, README.md, runtime manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
