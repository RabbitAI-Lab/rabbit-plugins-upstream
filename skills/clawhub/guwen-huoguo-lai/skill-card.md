## Description:

AI古文动画短视频创作：竞品分析→账号设计→脚本+提示词→发布策略。参考抖音AI教育号创建账号并持续产出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[shylamb-token](https://clawhub.ai/user/shylamb-token)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, educators, and content teams use this skill to plan AI-assisted short-video accounts and generate scripts, prompts, publishing copy, content calendars, and optional Word documents for ancient-Chinese literature animation videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trigger pattern may activate on unrelated account or video-planning requests.

Mitigation: Narrow the trigger or confirm the user's intent before applying the workflow.

Risk: The workflow relies on web browsing and public short-video page analysis, so extracted account metrics or style observations may be incomplete or stale.

Mitigation: Review sourced page data during use and treat platform metrics, comments, and style inferences as inputs to verify before publishing.

Risk: Generated educational content can include inaccurate classical text, exam-point, historical, or scientific claims.

Mitigation: Fact-check source passages, textbook wording, and subject-matter explanations before releasing videos.

Risk: The artifact can produce DOCX files through a Python script when requested.

Mitigation: Run generated scripts only in an appropriate agent environment and review output files before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shylamb-token/skills/guwen-huoguo-lai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with script templates, prompts, publishing plans, and optional DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May browse public short-video account pages, search the web, and write a Word document when the agent environment supports those tools.]

## Skill Version(s):

3.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
