## Description:

Imports an existing novel into a structured writing project for continued long- or short-form writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and writing-project teams use this skill to analyze an existing draft and rebuild it as a project they can continue writing. It routes long and short works to their respective analysis and project formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Import reads a manuscript and creates or updates files in the writing project.

Mitigation: Run from the intended workspace and review the selected book name and path before confirming.

Risk: Existing generated story assets or tracking state may be affected by an import.

Mitigation: Keep a backup of the existing project before importing.

## Reference(s):

- [ClawHub story-import release](https://clawhub.ai/worldwonderer/skills/story-import)
- [Project source link (skill metadata; import provenance unavailable)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Length routing](references/length-routing.md)
- [Long-form project mapping](references/structure-mapping-long.md)
- [Short-form project mapping](references/structure-mapping-short.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Configuration]

**Output Format:** [Local writing-project files and a Markdown import report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-form projects include outlines and tracking state; short-form projects use three single-file deliverables.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
