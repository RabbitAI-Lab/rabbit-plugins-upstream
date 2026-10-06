## Description:

Detects formulaic AI-style phrasing in Chinese web fiction and helps revise it into more natural prose while preserving story intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Writers and editors use this skill to identify repetitive or formulaic language in Chinese web fiction and revise passages or chapters while retaining character voice and plot details. It can also provide a detection-only report without modifying the text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Revision mode may alter targeted story files and change intended phrasing or story details.

Mitigation: Request detection-only mode when edits are unwanted; review file changes and flagged passages before accepting revisions.

Risk: Author-style preferences may persist in the project's .story/作者记忆 directory.

Mitigation: Review the author-memory behavior and stored preferences before using the skill in a project where persistent writing preferences are unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [Project link supplied in skill metadata (not verified provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Style resolution](references/style-resolution.md)
- [Author memory protocol](references/author-memory.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown diagnosis and revised Chinese prose; optionally edited story files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detection-only requests produce a report without edits; revision requests may update targeted story files and store author-style preferences in the project.]

## Skill Version(s):

1.1.26 (source: ClawHub release metadata; bundled skill frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
