## Description: <br>
Helps agents create, edit, optimize, deploy, manage, and analyze AI-Shifu courses, including MarkdownFlow Teaching Prompts, Course Prompts, learner progress, course revenue, ratings, and usage analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heshaofu2](https://clawhub.ai/user/heshaofu2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Course creators, educators, and AI-Shifu operators use this skill to turn source material into structured AI-Shifu lessons, maintain live course content, publish or archive courses, and inspect learner and business analytics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, modify, publish, archive, import, or delete AI-Shifu course content. <br>
Mitigation: Install only for trusted publishers and review destructive import, delete, publish, and archive actions before execution. <br>
Risk: The skill stores and reuses an AI-Shifu login token for creator access. <br>
Mitigation: Use only authorized AI-Shifu accounts, protect the local token file, and rotate or revoke credentials if the workspace is shared or compromised. <br>
Risk: The skill can query learner, revenue, rating, credit, and progress analytics. <br>
Mitigation: Limit use to courses and data the operator is authorized to access, and avoid exposing raw learner identifiers in public outputs. <br>
Risk: The skill sends usage telemetry unless disabled. <br>
Mitigation: Set AI_SHIFU_SKILL_TELEMETRY=off when telemetry is not appropriate for the environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator) <br>
- [AI-Shifu Course Creator Skill](SKILL.md) <br>
- [Course Design Intake](references/course-design-intake.md) <br>
- [Teaching Prompt](references/teaching-prompt.md) <br>
- [Course Prompt](references/course-prompt.md) <br>
- [MarkdownFlow Authoring](references/markdownflow-authoring.md) <br>
- [Course Analytics](references/analytics/workflow.md) <br>
- [CLI Reference](references/cli/cli-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, MarkdownFlow content, local course files, JSON-compatible analytics queries, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use AI-Shifu CLI commands that read or change live course state when the user authorizes platform access.] <br>

## Skill Version(s): <br>
1.2.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
