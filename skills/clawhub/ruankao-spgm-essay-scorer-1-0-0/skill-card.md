## Description: <br>
模拟阅卷评分软考高级资格「系统规划与管理师」的考生论文。当用户粘贴论文全文、询问"这篇论文能得多少分/帮我打分/模拟阅卷/论文质量评估/系规论文评分"时触发，按官方 5 维评分标准（切题性/实践性/深度与广度/逻辑性/书面表达）逐项打分、折算官方 75 分制得模拟分并判是否过线，对照 IMA 主库真题/范文/大纲给出针对性改进建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External exam candidates and study coaches use this skill to score draft System Planning and Management Engineer essays, check pass likelihood, identify red-line issues, and receive targeted revision guidance. The skill can optionally use an IMA knowledge base to compare against exam topics, rubrics, sample structures, and syllabus materials when the user authorizes lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional IMA lookup may send search queries derived from the essay topic or essay content to the knowledge-base integration. <br>
Mitigation: Use lookup only when the user is comfortable with that data flow; default scoring can fall back to bundled reference files without remote lookup. <br>
Risk: Generated reports include fixed author branding and a WeChat guidance referral. <br>
Mitigation: Review the branding and referral text before deployment so users understand the source and any contact pathway. <br>
Risk: Users may treat simulated exam scoring as official results or ask for substitute essay writing. <br>
Mitigation: Keep the disclaimer visible, provide critique and revision guidance only, and do not fabricate project details or write an essay on the user's behalf. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [IMA Knowledge Base Guide](references/ima_kb_guide.md) <br>
- [Project Background Template](references/project_bg_template.md) <br>
- [Scoring Rubric](references/scoring_rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, guidance] <br>
**Output Format:** [Markdown scoring report with tables, checklist items, pass/fail assessment, and revision guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a 75-point simulated score, five-dimensional scoring breakdown, red-line checks, and optional knowledge-base-backed improvement references.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
