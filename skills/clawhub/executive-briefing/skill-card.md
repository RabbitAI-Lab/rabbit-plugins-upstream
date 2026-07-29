## Description: <br>
高管汇报内容工厂 V2.0 — 输入详案→提炼为决策导向的高管报告。BLUF一页纸+So What叙事+脚本化工具链(init/bump/validate/density)。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dabin0927](https://clawhub.ai/user/dabin0927) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and business teams use this skill to turn detailed plans, research, or technical proposals into decision-oriented executive briefings, one-pagers, board briefings, and decision memos. It emphasizes BLUF structure, So What narrative, concise recommendations, and quality checks for executive readability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers and an automatic web-research handoff could expose sensitive report context without clear user consent. <br>
Mitigation: Require explicit confirmation before web research, and disable or manually approve research handoffs for confidential business plans. <br>
Risk: The included scripts create and update local report files, including versioned report copies and index files. <br>
Mitigation: Review the target directory before running file-changing commands, use dry-run options when available, and keep generated reports under version control or another backup process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dabin0927/skills/executive-briefing) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/dabin0927) <br>
- [README](README.md) <br>
- [Style guide](references/style-guide.md) <br>
- [Narrative methodology](references/narrative-methodology.md) <br>
- [Structure validation](references/structure-validation.md) <br>
- [Collaboration workflow](references/collaboration-workflow.md) <br>
- [Anthropic Executive Briefing reference](https://github.com/anthropics/executive-briefing) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports with optional HTML handoff, JSON validation reports, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report bodies target concise executive formats, including a documented 500-word limit for the main briefing body.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub server release metadata; artifact version.json reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
