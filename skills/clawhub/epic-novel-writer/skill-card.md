## Description:

Novel writing full workflow from world-building and character design to chapter planning, manuscript writing, version archiving, and HTML guide generation for medium to super-long serialized novels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

BSD-3-Clause

## Use Case:

External writers and creative teams use this skill to plan, draft, validate, and archive long-form serialized novels with consistent world-building, character tracking, global chapter numbering, and structured revision workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The archive workflow requires local file editing and shell execution, and the scanner notes that archive commands use a novel title as part of a filename template.

Mitigation: Use the skill only in a dedicated project folder, review commands before execution, and replace the novel title with a safe quoted filename or slug before creating archives.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunshinejnjn/skills/epic-novel-writer)
- [Project structure](references/project-structure.md)
- [Lifecycle](references/lifecycle.md)
- [Name rules](references/name-rules.md)
- [Archive template](references/archive-template.md)
- [World setting template](references/world-setting-template.md)
- [Character card template](references/character-card-template.md)
- [Chapter blueprint template](references/chapter-blueprint-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with file templates, inline shell commands, JSON examples, and HTML generation instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project files, character JSON, archive directories, merged manuscript text, and an HTML guide when the user requests those workflow steps.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
