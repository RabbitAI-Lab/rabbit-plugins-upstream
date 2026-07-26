## Description: <br>
Plan, draft, version, and refine written content with enforced versioning and quality audits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and content teams use this skill to plan, draft, revise, audit, and version written pieces while keeping drafts, research notes, and quality checks organized in a local workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The cleanup workflow can delete old version files for a selected piece. <br>
Mitigation: Run cleanup only after the piece is final, and verify the workspace path, piece ID, and retention count before confirming deletion. <br>
Risk: The skill can persist writing preferences by changing its own SKILL.md preference sections. <br>
Mitigation: Require explicit user approval before adding, removing, or rewriting persistent preferences. <br>
Risk: Drafts, research notes, audit reports, and versions are saved in a local workspace. <br>
Mitigation: Choose a workspace appropriate for the sensitivity of the content and review stored files before sharing or syncing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/haidiantoutou/skills/write) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Brief Reference](artifact/brief.md) <br>
- [Execution Reference](artifact/execution.md) <br>
- [Versioning Reference](artifact/versioning.md) <br>
- [Audit Reference](artifact/audit.md) <br>
- [Verification Reference](artifact/verification.md) <br>
- [Research Reference](artifact/research.md) <br>
- [State Reference](artifact/state.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and workspace file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create and update versioned writing files, research notes, audit reports, and workspace configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
