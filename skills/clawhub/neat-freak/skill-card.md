## Description: <br>
Neat Freak performs end-of-session knowledge cleanup by reconciling project documentation and agent memory with the codebase, then auditing whether workspace rules are being followed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kkkkhazix](https://clawhub.ai/user/kkkkhazix) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill at project milestones or session handoffs to keep README files, project docs, agent instructions, and agent memory aligned with the current codebase and workspace rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad cross-project and agent-memory access, which may expose unrelated projects or sensitive agent notes. <br>
Mitigation: Invoke it only in the intended workspace and constrain the cleanup scope before allowing reads or edits outside the active project. <br>
Risk: The workflow can make persistent documentation, memory, configuration, and deletion changes. <br>
Mitigation: Review planned edits and VCS diffs before accepting deletions or global memory/configuration updates. <br>


## Reference(s): <br>
- [Agent memory and configuration paths](references/agent-paths.md) <br>
- [Governance audit details](references/governance.md) <br>
- [Change impact matrix](references/sync-matrix.md) <br>
- [ClawHub skill page](https://clawhub.ai/kkkkhazix/skills/neat-freak) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and file-edit summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update project documentation, agent instruction files, and agent memory when the user authorizes the cleanup workflow.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
