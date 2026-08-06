## Description:

Story Import reverse-imports an existing draft or finished novel into a standard writing project, routing long-form and short-form works through the appropriate analysis and migration flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External authors and agent operators use this skill to import an existing manuscript into a continuation-ready writing project with analysis assets, migrated structure, and tracking state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update local writing-project files from a manuscript.

Mitigation: Run it only from the intended project workspace and review the detected book, title, and output path before confirming import.

Risk: Legacy tracking files may be moved into an archive folder during tracking initialization.

Mitigation: Review the project path before initialization and run the tracking check command after import to confirm the generated state and views are consistent.

## Reference(s):

- [Length Routing Rules](references/length-routing.md)
- [Long-Form Structure Mapping](references/structure-mapping-long.md)
- [Short-Form Structure Mapping](references/structure-mapping-short.md)
- [Tracking Transaction Protocol](references/tracking-transaction.md)
- [Character State Reverse Rules](references/character-state-reverse.md)
- [Format and Structure Rules](references/format-and-structure.md)
- [State Tracking Protocol](references/state-tracking.md)
- [OpenClaw Source Metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-import)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance, Files]

**Output Format:** [Markdown project files, JSON tracking state, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local writing-project directories and may archive legacy tracking files during initialization.]

## Skill Version(s):

1.0.14 (source: ClawHub release evidence; skill frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
