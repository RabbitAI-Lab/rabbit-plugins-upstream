## Description:

Checks Chinese web-novel prose for formulaic AI-like writing and polishes it while preserving the story's intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese web-novel authors and editors use this skill to identify repetitive or overly polished phrasing and revise prose without changing plot or characters. It can also report issues without editing when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Polishing in file mode modifies local manuscript files.

Mitigation: Request detection-only output to avoid edits; review manuscript changes before retaining them.

Risk: Optional author-style memory retains writing preferences in the project's .story/作者记忆 directory.

Mitigation: Review or remove that directory if you do not want those preferences retained.

## Reference(s):

- [ClawHub release](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [Project link declared in skill metadata (not verified release provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [AI writing and editing guide](artifact/references/anti-ai-writing.md)
- [Author-style memory guide](artifact/references/author-memory.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown issue reports and revised Chinese prose, including edited local text files in file mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detection-only requests produce reports without modifying source files.]

## Skill Version(s):

1.1.21 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
