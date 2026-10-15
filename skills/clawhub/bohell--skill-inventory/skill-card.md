## Description:

Skill Inventory scans installed skills, reads SKILL.md metadata, and generates or updates a workspace skills.md inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bohell](https://clawhub.ai/user/bohell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to list installed skills and refresh a skills.md inventory after installing, updating, or removing skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated inventory content may include unescaped metadata from third-party skills and influence later agent sessions.

Mitigation: Escape or validate skill metadata and treat generated inventory entries as data rather than instructions.

Risk: Running the script writes a persistent skills.md file in the workspace root.

Mitigation: Run it only in the intended workspace and review existing skills.md content before overwriting or relying on the generated inventory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bohell/skills/skill-inventory)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown file with console status messages and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes skills.md in the workspace root from SKILL.md metadata in the skills directory.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
