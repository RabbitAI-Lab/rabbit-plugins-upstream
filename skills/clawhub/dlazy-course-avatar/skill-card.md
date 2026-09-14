## Description:

Knowledge-course and online-teaching avatar lecturer guidance with 16 landscape base-portrait recipes and a slide-first pipeline for producing course videos with limited avatar screen time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, training teams, and developers use this skill to plan and generate AI lecturer course videos from course materials while keeping most lesson time focused on slides, narration, and structured assembly rather than full-time avatar footage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using a third-party CLI and service can expose local execution and service-trust risk.

Mitigation: Verify @dlazy/cli@1.2.3 before installation and prefer a project-local or sandboxed install.

Risk: Course documents, portraits, audio, videos, and optional API keys may be sent to dLazy services.

Mitigation: Only provide DLAZY_API_KEY and content that the user is comfortable sending to dLazy's service.

Risk: Generated course avatars and scripts can create compliance issues if they imply credentials, guaranteed outcomes, or unlabeled AI-generated instruction.

Mitigation: Review course copy and avatar visuals for fabricated credentials, training-effect promises, platform AI-labeling requirements, and legal approval before commercial publication.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [Pipeline guide](pipeline.md)
- [Recipe library](recipes.md)
- [Troubleshooting and compliance guide](troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with command examples and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workflow guidance for dLazy CLI usage; generated media files are produced by downstream tool calls, not by the skill card itself.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
