## Description: <br>
为任何主题生成结构化学习计划、练习题与进度追踪，支持自适应学习路径，适合个人用户日常快速上手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal learners use this skill to turn a topic into a staged study plan, practice questions, progress tracking, and a suggested adaptive learning path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests read, shell execution, and file-writing authority even though the release evidence describes it as mostly a Markdown-only learning assistant. <br>
Mitigation: Limit command execution and file-writing to explicit user-approved actions, and review proposed commands or file changes before allowing them. <br>
Risk: Generated learning plans, assessments, and practice material can be inaccurate or poorly matched to the learner's level. <br>
Mitigation: Treat outputs as study guidance to review and adapt, especially before using them for formal instruction or assessment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/learn-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional JSON, YAML, Python, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce structured learning plans, practice questions, progress summaries, configuration snippets, and local file or command suggestions when the agent permits those tools.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
