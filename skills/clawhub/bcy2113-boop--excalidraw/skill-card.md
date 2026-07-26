## Description: <br>
Generate, compress, and save .excalidraw.md drawings for the Obsidian Excalidraw plugin with element-bound arrows, LZ-String compression, and tree, flow, and architecture layout patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bcy2113-boop](https://clawhub.ai/user/bcy2113-boop) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to create Obsidian-compatible Excalidraw drawings, including architecture diagrams and tree or flow layouts with draggable, element-bound arrows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documentation includes a hardcoded Obsidian vault path and may write generated drawing files to that location. <br>
Mitigation: Review SKILL.md lines 10-15 before use and replace the path with the intended vault or output destination. <br>
Risk: Generated files may overwrite existing Obsidian notes or drawings when run unattended with an output path. <br>
Mitigation: Use an explicit output path, review destination filenames before execution, and avoid unattended writes where existing files may be present. <br>


## Reference(s): <br>
- [Excalidraw Patterns for Obsidian Plugin](artifact/references/patterns.md) <br>
- [Obsidian Excalidraw Plugin Release Reference](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag2.24.2) <br>
- [ClawHub skill page](https://clawhub.ai/bcy2113-boop/excalidraw) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [.excalidraw.md Markdown files containing YAML frontmatter, text elements, and LZ-String compressed JSON drawing data; may also include Excalidraw JSON and Node shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Obsidian Excalidraw plugin format with element-bound arrows and optional roundtrip verification by the compression helper.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
