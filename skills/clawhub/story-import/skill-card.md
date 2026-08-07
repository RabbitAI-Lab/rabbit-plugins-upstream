## Description:

Imports an existing long or short Chinese novel into a structured writing project so later writing skills can continue it from recovered source text, analysis assets, outlines, settings, and tracking state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External authors and writing-assistant users use this skill to convert an existing manuscript into a resumable story project. It supports long and short fiction by routing to the appropriate analysis pipeline and then rebuilding project files for follow-on writing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and modify a novel project in the workspace.

Mitigation: Review the target project path before running it and keep backups of important manuscripts.

Risk: Initialization may move old tracking files into a project archive.

Mitigation: Confirm the project is the intended import target before initialization and inspect the archived tracking files if migration is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-import)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Length routing rules](references/length-routing.md)
- [Long-form structure mapping](references/structure-mapping-long.md)
- [Short-form structure mapping](references/structure-mapping-short.md)
- [Tracking transaction protocol](references/tracking-transaction.md)
- [State tracking protocol](references/state-tracking.md)
- [Character state reverse rules](references/character-state-reverse.md)
- [Format and structure rules](references/format-and-structure.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with project file, JSON tracking-state, and shell-command instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or modifies workspace files for a novel-writing project and may move old tracking files into an archive during initialization.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
