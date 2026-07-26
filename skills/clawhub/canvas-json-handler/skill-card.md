## Description: <br>
Canvas Json Handler helps agents process JSON Canvas files for batch updates, template-based canvas creation, automatic layout, cross-canvas merging, repair, benchmarking, snapshots, and rollback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge engineers, process analysts, project managers, and operations teams use this skill to create, reorganize, merge, validate, and repair JSON Canvas workspaces with agent-assisted local file operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to run local commands and change canvas-related files. <br>
Mitigation: Use it only in a limited workspace and review proposed commands and file edits before applying them. <br>
Risk: Batch edits, merges, repairs, rollback, and cache-clearing actions may alter or remove useful canvas data. <br>
Mitigation: Request dry runs, backups, merge previews, or snapshots before applying broad changes. <br>
Risk: Automated repair may make incorrect assumptions about missing references, ID conflicts, or overlapping layout. <br>
Mitigation: Prefer conservative repair settings and manually review repair proposals before committing changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/canvas-json-handler) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, shell-command guidance, and generated or modified canvas-related files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce execution logs, status data, canvas snapshots, merge previews, repair proposals, and rollback guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
