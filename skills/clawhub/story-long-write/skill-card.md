## Description:

Story Long Write helps agents plan, draft, revise, and track long-form web novels, including worldbuilding, characters, plot lines, outlines, chapters, and continuity state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External writers and writing-assistant users use this skill to create and maintain long-form web-novel projects from initial concept through outlines, chapters, revisions, and continuity tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and edits story project files and may store local tracking or author-memory state.

Mitigation: Run it only in the intended writing workspace and review planned file changes before accepting them.

Risk: Bundled Python and Node.js checkers may execute locally during the writing workflow.

Mitigation: Inspect the bundled scripts and run them only in a trusted environment with normal workspace permissions.

Risk: Benchmark-book or beat-by-beat adaptation workflows could produce outputs too close to copyrighted source works.

Mitigation: Use licensed, public-domain, or high-level genre references and review generated outlines or chapters for originality.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-write)
- [OpenClaw metadata source](https://github.com/zenstory-ai/oh-story-claudecode)
- [Skill definition](artifact/SKILL.md)
- [Setup workflow](artifact/references/workflow-setup.md)
- [Chapter workflow](artifact/references/workflow-chapter.md)
- [Daily writing workflow](artifact/references/workflow-daily.md)
- [Revision workflow](artifact/references/workflow-revision.md)
- [Long-form writing guide](artifact/references/long-format.md)
- [Writing craft guide](artifact/references/writing-craft.md)
- [Reader contract and progression](artifact/references/reader-contract-and-progression.md)
- [Author memory](artifact/references/author-memory.md)
- [Artifact protocols](artifact/references/artifact-protocols.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose, project files, JSON tracking state, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and edits story project files, may run bundled Python and Node.js checkers, and can maintain local tracking plus optional author-memory state.]

## Skill Version(s):

1.1.22 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
