## Description:

Use when two skills fire for the same request, or a skill never fires at all — scans every installed skill, maps trigger overlaps and blind spots, delivers one health report with fixes. 当多个技能被同一句话触发、或某个技能从不触发时使用——扫描全部已装技能，找出触发重叠与盲区，输出一份带修复建议的体检报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomaszhou22](https://clawhub.ai/user/thomaszhou22)

### License/Terms of Use:

MIT

## Use Case:

Developers who maintain agent skills use this skill to find trigger conflicts, uncovered tasks, weak descriptions, duplicates, and rarely used skills. It produces a health report with concrete description improvement proposals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested description edits may be incorrect or may change which requests activate a skill.

Mitigation: Review the exact description diffs and scan the descriptions again before applying changes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/thomaszhou22/skills/skill-health-checkup)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown health report with tables and proposed description edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One report; proposed description changes should be reviewed before application.]

## Skill Version(s):

1.0.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
