## Description:

Create deterministic hand-drawn, whiteboard, educational, and explainer MP4 animations from a JSON Animation DSL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT

## Use Case:

Developers and content creators use this skill to create, validate, render, and verify deterministic SVG-first MP4 whiteboard or explainer animations from a JSON project file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendering unreviewed third-party SVG or project content may introduce unsafe or misleading content into the browser-based render path.

Mitigation: Render only trusted project JSON and SVG assets, review third-party assets before use, and validate the project before rendering.

Risk: Narration text can be sent to the external Edge TTS service when optional narration is enabled.

Mitigation: Avoid sensitive or proprietary narration text, or omit narration for local-only rendering.

Risk: Installation and sync scripts install dependencies and update local agent skill directories.

Mitigation: Review dependency installation and sync scripts before running them.

## Reference(s):

- [Animation DSL v1](references/dsl.md)
- [Installing HandDraw Skill in Other Agents](references/agent-installation.md)
- [Narrative character system](references/narrative-character-system.md)
- [Server-resolved GitHub provenance](https://github.com/ToBeWin/HandDraw-Skill)
- [ClawHub skill page](https://clawhub.ai/tobewin/skills/handdraw-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON DSL snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or edits local project JSON, SVG asset guidance, render commands, and MP4 verification steps.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
