## Description: <br>
AI-Shifu Course Creator helps agents create, edit, optimize, deploy, manage, and analyze AI-Shifu courses, Teaching Prompts, Course Prompts, and MarkdownFlow course artifacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heshaofu2](https://clawhub.ai/user/heshaofu2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Course authors, operators, and developers use this skill to turn source material into AI-Shifu course artifacts, update existing platform courses, publish or manage courses, and query live-course analytics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stored account access may be reused for course mutations, publishing or archive actions, image uploads, and learner or order analytics. <br>
Mitigation: Install only when that account authority is acceptable, and require explicit user confirmation before existing-course import, publish or archive, bulk deletion, or broad learner analytics queries. <br>
Risk: Existing-course import can replace course structure and content, which may delete and recreate outlines and change platform state. <br>
Mitigation: Confirm the intended target course and destructive import scope before execution, then verify the resulting course state after the operation. <br>
Risk: Learner analytics can expose sensitive course, learner, order, revenue, or progress information. <br>
Mitigation: Limit analytics queries to the requested course and question, avoid exposing raw learner identifiers, and summarize only the minimum necessary results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator) <br>
- [Platform Authentication](references/authentication.md) <br>
- [Course Design Intake](references/course-design-intake.md) <br>
- [Orchestration Workflow](references/orchestration-workflow.md) <br>
- [Teaching Prompt](references/teaching-prompt.md) <br>
- [Course Prompt](references/course-prompt.md) <br>
- [MarkdownFlow Spec](references/markdownflow.md) <br>
- [New Course Deployment](references/deployment-workflow.md) <br>
- [Course Management](references/course-management.md) <br>
- [Course Analytics](references/analytics/workflow.md) <br>
- [Privacy & Presentation](references/analytics/privacy-and-presentation.md) <br>
- [CLI Reference](references/cli/cli-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, MarkdownFlow prompt content, local course files, and shell command recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update AI-Shifu course directories, Teaching Prompts, Course Prompts, course descriptions, analytics reports, and CLI command sequences.] <br>

## Skill Version(s): <br>
1.2.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
