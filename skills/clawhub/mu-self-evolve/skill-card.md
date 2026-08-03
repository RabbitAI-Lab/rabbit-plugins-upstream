## Description: <br>
Agent自我反思与进化器 helps AI agents convert daily corrections, errors, feedback, and recurring patterns into structured local learning records, verified long-term memory updates, and weekly reflection workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[muippt](https://clawhub.ai/user/muippt) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to maintain local self-improvement records, verify recurring patterns before promoting them into long-term guidance, prune stale memories, and draft new skills from repeated knowledge clusters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist conversation details into local learning and error records. <br>
Mitigation: Review the skill before installing, and do not allow tokens, secrets, auth headers, or detailed credential state to be stored in logs. <br>
Risk: The skill can update long-term agent guidance such as memory, tool, soul, or agent instruction files. <br>
Mitigation: Require human review before accepting changes to MEMORY, SOUL, TOOLS, or AGENTS guidance files. <br>
Risk: Scheduled runs can repeatedly read daily memory notes and write persistent learning files. <br>
Mitigation: Disable or avoid scheduled runs until the operator is comfortable with the scope of the workflow. <br>


## Reference(s): <br>
- [Record Templates](references/record-templates.md) <br>
- [Weekly Reflection Workflow](references/weekly-reflection.md) <br>
- [File Structure and Tags](references/file-structure.md) <br>
- [Claude Code Compatibility](references/claude-code-compat.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/muippt/skills/mu-self-evolve) <br>
- [Project Landing Page](https://muippt.github.io/mu-self-evolve/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, local file templates, and Python script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces and updates local markdown learning records and may generate skill drafts for human review.] <br>

## Skill Version(s): <br>
3.0.0 (source: release metadata and changelog, released 2026-07-21) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
