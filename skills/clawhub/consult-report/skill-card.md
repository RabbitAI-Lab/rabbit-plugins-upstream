## Description: <br>
战略/市场分析咨询报告工作流——判断+数据双轨。先出有排他性的框架判断,再用真实数据验证(数据文件或公开信息),输出结构化 Markdown 咨询报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuobadaidai](https://clawhub.ai/user/tuobadaidai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business analysts, strategists, and market researchers use this skill to create Chinese-first consulting reports for market entry, industry analysis, competitive analysis, strategic diagnosis, and growth strategy questions. It emphasizes hypothesis-led judgment, evidence-backed data validation, and structured Markdown reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Consulting conclusions can be misleading if source data is incomplete, stale, or unverifiable. <br>
Mitigation: Use the skill's evidence rules to label each key number by source, method, timeliness, and confidence, and downgrade unsupported conclusions to unverified. <br>
Risk: User-provided files may contain sensitive business data. <br>
Mitigation: Provide only files intended for analysis and keep report outputs aligned with the intended audience and sharing boundary. <br>
Risk: Complex S-level tasks may rely on parallel subagents when the host environment supports them. <br>
Mitigation: Review subagent findings before relying on the final report, and note when independent validation could not be performed. <br>


## Reference(s): <br>
- [Data Analysis Discipline](artifact/references/data-analysis.md) <br>
- [Report Output Specification](artifact/references/output-spec.md) <br>
- [ClawHub Release Page](https://clawhub.ai/tuobadaidai/skills/consult-report) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Structured Markdown consulting report with cited data, tables, and optional chart artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Python analysis steps, source annotations, confidence labels, and explicit limitation notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
