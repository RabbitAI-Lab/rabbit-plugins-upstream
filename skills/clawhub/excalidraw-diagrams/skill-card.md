## Description:

Builds deterministic Excalidraw drawings from a boxes-and-arrows spec, with layout and bindings. Produces Obsidian .excalidraw.md notes or .excalidraw files. Use only for explicit Excalidraw requests, including Excalidraw in Obsidian.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Obsidian users use the skill to turn an explicit boxes-and-arrows specification into a laid-out Excalidraw diagram saved as an Obsidian note or a standalone file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagram labels are stored as plain text and may expose information included in the drawing.

Mitigation: Keep sensitive details out of diagram labels and specs.

Risk: Compressed Obsidian drawings receive frontmatter-only validation until decompressed.

Mitigation: Decompress the drawing in Obsidian and rerun scene validation before relying on full validation.

Risk: An unintended destination or overwrite can put a drawing in the wrong place or replace prior work.

Mitigation: Choose the destination explicitly and authorize any overwrite before using --force.

## Reference(s):

- [Excalidraw file format reference](references/excalidraw-format.md)
- [Project homepage](https://github.com/Ricardodpalmeida/openclaw-excalidraw-diagrams)
- [ClawHub listing](https://clawhub.ai/ricardodpalmeida/skills/excalidraw-diagrams)
- [Excalidraw](https://excalidraw.com)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown]

**Output Format:** [Excalidraw JSON (.excalidraw) or an Obsidian Markdown note (.excalidraw.md)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic layout and bindings; requires Python 3.9 or newer.]

## Skill Version(s):

1.1.5 (source: changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
