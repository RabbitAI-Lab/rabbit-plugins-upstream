## Description:

Helps agents create, edit, optimize, deploy, manage, and analyze AI-Shifu courses, including MarkdownFlow teaching prompts, course prompts, live course operations, and course analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, operators, and supporting agents use this skill to turn source material into AI-Shifu course content, publish or update courses through the platform CLI, and answer creator analytics questions about learners, orders, revenue, ratings, and credit use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI reports usage telemetry that can be linked to a logged-in platform user and includes command name, skill version, host agent, and platform information.

Mitigation: Set AI_SHIFU_SKILL_TELEMETRY=off when command telemetry is not desired; the artifact states telemetry does not send course content, command arguments, file paths, titles, or tokens.

Risk: The skill can make live course changes, including import, publish, archive, reorder, metadata updates, lesson access changes, and existing-course content replacement.

Mitigation: Require explicit human confirmation before publish, archive, delete, reorder, import into an existing course, or other learner-facing mutations, and verify CLI-produced URLs and readbacks after each write.

Risk: A custom SHIFU_BASE_URL could route authentication and course operations to an untrusted host.

Mitigation: Use the default AI-Shifu host or only a trusted HTTPS SHIFU_BASE_URL before login or mutation commands.

Risk: Dependency minimums may allow installation of older versions than currently patched releases.

Mitigation: Install current patched dependency versions instead of the oldest versions accepted by requirements.txt.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator)
- [AI-Shifu platform](https://app.ai-shifu.cn)
- [CLI Reference](references/cli/cli-reference.md)
- [Course Directory Specification](references/cli/course-directory-spec.md)
- [MarkdownFlow](references/markdownflow.md)
- [Deployment Workflow](references/deployment-workflow.md)
- [Course Management](references/course-management.md)
- [Analytics Privacy and Presentation](references/analytics/privacy-and-presentation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, configuration snippets, and generated course files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local course directories, MarkdownFlow prompt files, import JSON, CLI commands, platform verification URLs, and analytics summaries.]

## Skill Version(s):

1.2.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
