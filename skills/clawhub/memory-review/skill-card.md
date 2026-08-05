## Description: <br>
Review daily memory logs and consolidate durable knowledge into the existing memory hierarchy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[axelhu](https://clawhub.ai/user/axelhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to turn daily memory logs into durable, current workspace knowledge while preferring updates to existing canonical documents over creating duplicates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Memory files may contain sensitive operational context. <br>
Mitigation: Install only in workspaces where the agent is allowed to review daily logs and update canonical memory files. <br>
Risk: Incorrect memory consolidation can preserve stale or misleading guidance. <br>
Mitigation: Review generated decision plans and diffs before accepting changes, and defer signals that lack stable evidence. <br>


## Reference(s): <br>
- [Memory Review Specification](references/spec.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/axelhu/skills/memory-review) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown reports, JSON decision and scan plans, local memory file edits, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes are constrained to memory knowledge, project, glossary, post-mortem, daily report, execution log, and scan-state paths described by the skill.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
