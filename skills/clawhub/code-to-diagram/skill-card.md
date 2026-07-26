## Description: <br>
Analyzes source-code logic, generates Mermaid flowcharts or SVG architecture diagrams, and can render them as PNG images with Mermaid themes, visual styles, semantic diagram shapes, and product icons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhouchang1988](https://clawhub.ai/user/zhouchang1988) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to inspect source files, choose an appropriate Mermaid or SVG diagram style, and produce documentation-ready diagrams for code flows, architecture, data models, and agent systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local Node rendering commands. <br>
Mitigation: Review commands before execution and run the skill in a workspace where local rendering tools are expected. <br>
Risk: The Mermaid renderer may fall back to an unpinned npx invocation. <br>
Mitigation: Install Mermaid CLI from a trusted, pinned source before use and prefer that installed renderer over the fallback. <br>
Risk: Mermaid input files passed to the renderer may be deleted automatically after rendering. <br>
Mitigation: Use scratch or generated .mmd files for rendering, or keep backups of any source Mermaid files before running the renderer. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Optimization Plan](docs/optimization-plan.md) <br>
- [Icon Reference](references/icons.md) <br>
- [Diagram Style Matrix](references/style-diagram-matrix.md) <br>
- [Flat Icon Style](references/style-1-flat-icon.md) <br>
- [Dark Terminal Style](references/style-2-dark-terminal.md) <br>
- [Blueprint Style](references/style-3-blueprint.md) <br>
- [Notion Clean Style](references/style-4-notion-clean.md) <br>
- [Glassmorphism Style](references/style-5-glassmorphism.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown documentation with Mermaid or SVG code blocks, optional PNG image files, and renderer JSON output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Mermaid rendering may use mmdc or an npx fallback; SVG rendering uses rsvg-convert when PNG output is requested.] <br>

## Skill Version(s): <br>
3.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
