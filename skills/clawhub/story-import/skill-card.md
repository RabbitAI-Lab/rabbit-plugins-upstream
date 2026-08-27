## Description:

Story Import reverse-engineers an existing draft or completed novel into a standard writing-project structure for continued writing with story-long-write or story-short-write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and writing-workflow developers use this skill to import an existing novel, analyze it by length, and rebuild it as a reusable project with source text, analysis assets, outlines, settings, manuscript files, and tracking state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update writing-project files, analysis directories, tracking archives, and .active-book.

Mitigation: Run it only in the intended writing project and use version control or backups before importing a large or existing project.

Risk: Imported structure and tracking state may be incomplete or incorrect if the source novel is ambiguous or partially drafted.

Mitigation: Review generated settings, outlines, manuscript files, and tracking state before continuing the story workflow.

## Reference(s):

- [Story Import ClawHub Page](https://clawhub.ai/worldwonderer/skills/story-import)
- [OpenClaw Source Metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Format and Structure](references/format-and-structure.md)
- [Length Routing](references/length-routing.md)
- [Long Structure Mapping](references/structure-mapping-long.md)
- [Short Structure Mapping](references/structure-mapping-short.md)
- [State Tracking](references/state-tracking.md)
- [Tracking Transaction](references/tracking-transaction.md)
- [Character State Reverse](references/character-state-reverse.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON-backed local project files, with concise command guidance when helper scripts are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create analysis and project directories, archive older tracking data, and update .active-book in the target writing project.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
