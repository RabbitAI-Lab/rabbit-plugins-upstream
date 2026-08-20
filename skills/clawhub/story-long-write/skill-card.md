## Description:

Supports long-form web fiction workflows from concept and outline through chapter drafting, revision, story-state tracking, and genre-specific prose guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing teams use this skill to plan Chinese long-form web novels, manage story files and continuity, draft selected chapters, revise chapters, and apply genre-specific writing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and write story project files and mutate outlines, chapters, settings, and tracking state.

Mitigation: Install and run it only in a dedicated writing workspace, and review file changes before using them as authoritative project state.

Risk: The skill may look one directory up for planning inputs, copy benchmark or reference material, run bundled Python and Node scripts, and invoke optional local agents.

Mitigation: Review the workspace layout, bundled scripts, and optional agent configuration before execution; limit access to files intended for the writing project.

Risk: The skill includes source-work adaptation guidance that could encourage close copying of reference works.

Mitigation: Use reference material for high-level structure and craft analysis only, and avoid direct reuse of copyrighted plots, scenes, phrasing, or style.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-write)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Workflow setup](references/workflow-setup.md)
- [Workflow daily](references/workflow-daily.md)
- [Workflow revision](references/workflow-revision.md)
- [Reader contract and progression](references/reader-contract-and-progression.md)
- [Artifact protocols](references/artifact-protocols.md)
- [Genre prose cards](references/genre-prose-cards.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose, structured story files, JSON state, and inline shell or script commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update project files for outlines, chapters, settings, character state, continuity tracking, and benchmark/reference views.]

## Skill Version(s):

1.1.19 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
