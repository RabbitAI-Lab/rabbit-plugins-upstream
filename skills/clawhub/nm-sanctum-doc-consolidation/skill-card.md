## Description: <br>
Merges ephemeral report and analysis artifacts into permanent documentation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to identify temporary LLM-generated Markdown reports, route valuable sections into durable documentation, and clean up source artifacts after approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approved consolidation can delete source Markdown reports after successful merges, and rollback may not restore those originals automatically. <br>
Mitigation: Review the consolidation plan before approval, especially destination files and source files marked for deletion; keep external backups or commit/restore points for important reports. <br>
Risk: Misrouted or low-value report content can introduce inaccurate or misleading material into permanent documentation. <br>
Mitigation: Review proposed destinations, merge strategies, and generated documentation changes before committing the results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-doc-consolidation) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown plans, documentation edits, and execution summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user approval before merge execution; source Markdown files may be deleted after successful consolidation.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
