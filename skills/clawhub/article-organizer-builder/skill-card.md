## Description:

Builds a customized Obsidian article-organizing skill that scans Markdown articles, proposes deduplication and classification rules, generates structured notes, and safely archives processed source files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kakahilda](https://clawhub.ai/user/kakahilda)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this builder to create a personalized Obsidian workflow skill for collecting, deduplicating, classifying, and archiving web or public-account articles as structured notes. The generated skill is intended to create a new standalone skill directory based on user-provided paths, classification rules, tags, and note-title preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated skill can create scripts that move article files and same-named attachment folders after processing.

Mitigation: Review the generated skill directory before use and confirm the vault, source, favorites, and archive paths match the intended workspace.

Risk: Incorrect user-provided paths or classification rules could cause notes to be organized in the wrong location or taxonomy.

Mitigation: Validate the generated directory overview, classification rules, tag mapping, and acceptance checklist before running generated scan or cleanup commands.

## Reference(s):

- [Builder Prompt](references/builder-prompt.md)
- [ClawHub Skill Page](https://clawhub.ai/kakahilda/skills/article-organizer-builder)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance plus a generated skill directory containing SKILL.md, Python scripts, and reference documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated scripts are specified to use only the Python standard library and to preserve archive-first cleanup behavior.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
