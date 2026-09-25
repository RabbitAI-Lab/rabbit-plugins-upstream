## Description:

Imports an existing novel into a structured writing project, analyzing the manuscript and routing short and long works to their respective continuation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and writing assistants use this skill to turn an existing unfinished or completed novel into a structured project with manuscript analysis, outlines, character information, and tracking files for later writing or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Import reads the manuscript and creates or updates files in the selected writing-project directory.

Mitigation: Review the manuscript and target project path before running the import.

Risk: Initialization may move existing tracking files into an archive within the project.

Mitigation: Check any existing 追踪/ directory and retain a backup before initialization.

## Reference(s):

- [ClawHub release: story-import](https://clawhub.ai/worldwonderer/skills/story-import)
- [Project link listed in skill metadata (not verified import provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Length routing](references/length-routing.md)
- [Long-form project mapping](references/structure-mapping-long.md)
- [Short-form project mapping](references/structure-mapping-short.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Files]

**Output Format:** [Writing-project files and a Markdown import report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates manuscript, analysis, outline, and tracking files for subsequent writing.]

## Skill Version(s):

1.0.22 (source: ClawHub release; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
