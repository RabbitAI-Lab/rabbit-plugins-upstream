## Description:

Long-form web novel writing support that helps an agent plan, draft, revise, and track novel projects from outline through chapter prose.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through long-form Chinese web novel workflows, including project setup, character and plot planning, chapter drafting, revisions, and continuity tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A bundled tracking script can delete Markdown files outside the project through a symlink.

Mitigation: Use only in trusted, private workspaces; avoid untrusted or shared projects until this issue is fixed, and review symlinks before running file-management workflows.

Risk: Author-memory files are written with permissive local permissions.

Mitigation: Keep workspaces private, avoid storing sensitive personal material in author memory, and adjust local file permissions when needed.

Risk: Plot-adaptation and viewpoint guidance may reflect opinionated writing rules rather than neutral advice.

Mitigation: Review generated guidance and prose for originality, editorial fit, and alignment with the author’s intent before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-write)
- [Publisher profile](https://clawhub.ai/user/worldwonderer)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Reference index](references/reference-index.md)
- [Setup workflow](references/workflow-setup.md)
- [Chapter workflow](references/workflow-chapter.md)
- [Daily writing workflow](references/workflow-daily.md)
- [Revision workflow](references/workflow-revision.md)
- [Project files protocol](references/project-files.md)
- [Author memory protocol](references/author-memory.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and workspace project files, with optional shell commands for bundled checks and tracking utilities]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local novel planning, draft, reference, and tracking files.]

## Skill Version(s):

1.1.23 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
