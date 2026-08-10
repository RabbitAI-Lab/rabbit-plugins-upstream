## Description:

Imports an existing completed or in-progress novel into a structured writing project that can be continued through related long-form or short-form story-writing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and writing-workflow users use this skill to import an existing novel from a file, directory, or pasted text, analyze it by length, and rebuild it as a continuation-ready project with source analysis, settings, outline, manuscript, and tracking assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-provided novel source files and creates or updates local writing-project directories.

Mitigation: Invoke it explicitly with /story-import, review the detected source path and book title before confirming, and keep backups before large imports.

Risk: Large imports can make broad local file changes as part of rebuilding a continuation-ready writing project.

Mitigation: Review the generated project structure and tracking assets before using downstream writing workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-import)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Length routing rules](references/length-routing.md)
- [Long-form structure mapping](references/structure-mapping-long.md)
- [Short-form structure mapping](references/structure-mapping-short.md)
- [Tracking transaction protocol](references/tracking-transaction.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated project files, JSON tracking state, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local writing-project directories and analysis assets for the imported novel.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
