## Description:

This skill analyzes long web novels in staged chapter batches and produces chapter summaries, plot and pacing analysis, character and setting notes, and a style profile while supporting continuation of existing work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and literary analysts use this skill to examine a long novel's chapter events, story structure, reader-facing pacing, characters, settings, and prose style. It creates reusable notes that can support later writing decisions or continuation of an existing analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Novel source copies and analysis caches remain in the workspace after analysis.

Mitigation: Use a dedicated writing workspace and account for the retained source and cache files when managing project data.

Risk: When several projects share a directory, an automatic topic update could select an unintended 选题决策.md file.

Mitigation: Check which 选题决策.md file the automatic topic update will select before running the update.

## Reference(s):

- [Declared source repository (from skill metadata)](https://github.com/zenstory-ai/oh-story-claudecode)
- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/story-long-analyze)

## Skill Output:

**Output Type(s):** [Text analysis, Markdown reports, CSV indexes, Relationship diagrams]

**Output Format:** [Markdown documents, CSV data, and diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Organized as per-book analysis files that can be resumed and extended.]

## Skill Version(s):

1.1.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
