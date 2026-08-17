## Description:

Audits scheduled automation token usage, evaluates consolidation opportunities, identifies redundant tasks, and produces an optimization report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to review scheduled automations, identify high token consumption, and decide which tasks can be merged, deleted, reduced in frequency, scripted, or simplified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad authority to review and change scheduled automations.

Mitigation: Run a dry review first and require explicit user confirmation before any task update, merge, or deletion.

Risk: Replaced tasks may be deleted without a fresh confirmation step.

Mitigation: Confirm that replacement tasks fully preserve required behavior and obtain approval before deletion.

Risk: Outputs may include unrelated promotional contact information.

Mitigation: Review generated reports and remove unrelated promotional content before sharing or archiving them.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown report with tables, checklists, and optional shell or Python script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May inspect scheduled automation metadata and local usage data before recommending task updates, merges, deletions, or frequency changes.]

## Skill Version(s):

2.0.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
