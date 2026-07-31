## Description: <br>
Report Builder turns long source material into concise executive briefings, decision memos, one-pagers, and board briefings with templates and local validation scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dabin0927](https://clawhub.ai/user/dabin0927) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external consultants, and business operators use this skill to convert detailed plans, research, or decision material into executive-ready Markdown reports for CEOs, boards, investors, and department leaders. It is intended for decision support rather than technical documentation, data analysis, slide design, or visual formatting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local scripts create and update report files, including version.json, README.md, VERSION.md, and copied Markdown report versions. <br>
Mitigation: Review the target directory before running init.py, bump.py, or renumber.py, and use dry-run mode where available before accepting file changes. <br>
Risk: Executive reports can mislead decision-makers if prompts are vague or source material is incomplete. <br>
Mitigation: Provide specific report goals, audience, decision context, and source material, then review generated reports before sharing. <br>


## Reference(s): <br>
- [Report Builder on ClawHub](https://clawhub.ai/dabin0927/skills/executive-briefing) <br>
- [Style Guide](references/style-guide.md) <br>
- [Narrative Methodology](references/narrative-methodology.md) <br>
- [Structure Validation](references/structure-validation.md) <br>
- [Collaboration Workflow](references/collaboration-workflow.md) <br>
- [Edge Cases](references/edge-cases.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports and templates, JSON validation output, shell-command guidance, and copied versioned report files; HTML output is delegated to a downstream markdown-to-html skill.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3. Local scripts may create report folders and update version.json, README.md, VERSION.md, and copied Markdown report versions.] <br>

## Skill Version(s): <br>
2.1.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
