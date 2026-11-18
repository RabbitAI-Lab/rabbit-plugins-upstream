## Description:

Records an authorized browser workflow and turns it into a reusable automation skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yysws5566](https://clawhub.ai/user/yysws5566)

### License/Terms of Use:

MIT-0

## Use Case:

Operators and developers use the skill to record repetitive tasks in browser sessions they are authorized to access, review the captured workflow, and create reusable automation for later runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recorded browser data may expose account or other sensitive information, and scanner coverage was incomplete.

Mitigation: Review captured files and data handling before installation, keep recordings access-controlled, and remove them when no longer needed. Treat the suspicious verdict as a review signal; it does not establish malicious intent.

Risk: Automation may exceed its intended execution scope or perform actions without the expected approval.

Mitigation: Review the execution scope and approval safeguards before use, and require explicit operator approval for production changes.

Risk: Browser cleanup behavior may not match expectations.

Mitigation: Review cleanup behavior and confirm which browser processes the skill may close before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yysws5566/skills/skill-forge)
- [CDP troubleshooting and evidence capture](references/CDP排障与采证.md)
- [Local file reading guide](references/本地文件读取.md)
- [Packaging and acceptance guide](references/打包与验收.md)
- [Tested status notes](references/实测状态.md)

## Skill Output:

**Output Type(s):** [Code, Files, Configuration, Shell commands, Guidance]

**Output Format:** [JavaScript and Python scripts, JSON and CSV artifacts, and Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files vary with the recorded workflow and selected automation path.]

## Skill Version(s):

2.2.0 (source: server release, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
