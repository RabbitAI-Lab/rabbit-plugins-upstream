## Description:

Builds deterministic Excalidraw drawings from a boxes-and-arrows spec, with layout and bindings. Produces Obsidian .excalidraw.md notes or .excalidraw files. Use only for explicit Excalidraw requests, including Excalidraw in Obsidian.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can turn an explicitly requested boxes-and-arrows description into an editable Excalidraw diagram for Obsidian or excalidraw.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was incomplete because one path-like reference was unresolved, and the host runtime's file access can affect the impact of using the skill.

Mitigation: Review unresolved path references and limit the host runtime's file access to what the diagram task requires.

## Reference(s):

- [Excalidraw file format reference](references/excalidraw-format.md)
- [ClawHub skill page](https://clawhub.ai/ricardodpalmeida/skills/excalidraw-diagrams)
- [Source repository homepage](https://github.com/Ricardodpalmeida/openclaw-excalidraw-diagrams)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown]

**Output Format:** [Excalidraw JSON (.excalidraw) or Obsidian Markdown with embedded Excalidraw JSON (.excalidraw.md)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Editable diagram with layout, labels, and bindings; includes the output path, diagram counts, warnings, and visual inspection status.]

## Skill Version(s):

1.1.8 (source: CHANGELOG, released 2026-11-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
