## Description:

Detects formulaic AI-writing patterns in Chinese web fiction and helps authors revise the prose while preserving its plot and voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese web-fiction authors and editors use this skill to identify repetitive or overly polished phrasing and revise selected passages or story files without changing the underlying narrative. Detection-only requests can return findings without editing the text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Revision mode can overwrite user-selected story files in place.

Mitigation: Request detection-only mode when edits are unwanted; review changes to selected files before accepting them.

Risk: Explicit long-term writing preferences may persist in project or book author-style memory for future reuse.

Mitigation: Store only preferences the author explicitly asks to retain, and review or remove stored preferences when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [Declared source link in skill metadata (not verified provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Writing guidance](artifact/references/anti-ai-writing.md)
- [Author-style memory guidance](artifact/references/author-memory.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown diagnosis and revision report, with revised prose in the response or in selected story files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detection-only mode reports findings without edits; file mode can modify selected story files in place.]

## Skill Version(s):

1.1.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
