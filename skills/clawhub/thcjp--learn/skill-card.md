## Description:

Helps learners structure study plans, review cards, active-recall prompts, and progress checks using spaced repetition and active recall across domains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Learners, educators, and productivity-focused agent users use this skill to turn a learning topic and study method preference into learning paths, spaced-review items, active-recall prompts, and progress assessments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command-execution capabilities that may affect files or the local environment.

Mitigation: Run it only in a constrained workspace and require explicit approval before file modification or shell command execution.

Risk: The skill includes API-key setup guidance and may lead users to provide credentials.

Mitigation: Avoid entering real API keys unless the destination service is clear, and keep credentials out of shared files and version control.

Risk: Learning outputs such as plans, recall questions, and progress assessments can be inaccurate or poorly matched to the user's goals.

Mitigation: Review generated study materials before relying on them and keep the skill focused on non-sensitive learning content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/learn)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file operations, API-key setup, or command execution that should be reviewed before use.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
