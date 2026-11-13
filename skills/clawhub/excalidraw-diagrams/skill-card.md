## Description:

Builds deterministic Excalidraw drawings from a boxes-and-arrows spec, with layout and bindings, and produces Obsidian .excalidraw.md notes or .excalidraw files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can turn a requested boxes-and-arrows diagram into an editable Excalidraw drawing for Obsidian or excalidraw.com. The skill is intended for explicit Excalidraw requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a benign verdict with medium confidence and partial scan coverage; it notes file read and write capabilities, and that the host runtime's permissions were not verified.

Mitigation: Review the unresolved path-like reference and limit the skill's filesystem access to the intended diagram files.

## Reference(s):

- [ClawHub release](https://clawhub.ai/ricardodpalmeida/skills/excalidraw-diagrams)
- [Project homepage](https://github.com/Ricardodpalmeida/openclaw-excalidraw-diagrams)
- [Excalidraw format reference](references/excalidraw-format.md)
- [Obsidian Excalidraw plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown]

**Output Format:** [Excalidraw scene files (.excalidraw) or Obsidian Markdown notes with embedded Excalidraw scenes (.excalidraw.md)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Editable diagrams with deterministic layout, labels and bound arrows.]

## Skill Version(s):

1.1.7 (source: server-resolved release and CHANGELOG.md, released 2026-11-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
