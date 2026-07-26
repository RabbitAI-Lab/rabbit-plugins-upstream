## Description: <br>
Professional Figma design analysis and asset export for extracting design data, exporting assets, auditing accessibility and design systems, and generating design documentation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maddiedreese](https://clawhub.ai/user/maddiedreese) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, designers, and design-system teams use this skill to inspect Figma files, export assets and design tokens, and generate accessibility, style, and handoff reports from read-only Figma API data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Figma token may allow access to every file and team resource available to that token. <br>
Mitigation: Use the least-privileged token available, pass it through an environment variable or secret manager, and keep it out of source control and logs. <br>
Risk: Exports and reports write local files and may overwrite existing output if paths are reused. <br>
Mitigation: Send exports and reports to a dedicated output directory and review output paths before running commands. <br>


## Reference(s): <br>
- [Figma API Reference](references/figma-api-reference.md) <br>
- [Design Patterns and Component Best Practices](references/design-patterns.md) <br>
- [Accessibility Guidelines for Figma Design](references/accessibility-guidelines.md) <br>
- [Export Formats and Specifications](references/export-formats.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated reports and export artifacts may be JSON, HTML, CSS, SCSS, JavaScript, PNG, SVG, PDF, or WEBP.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads Figma API data through a user-provided token and writes exports or reports to user-selected output paths.] <br>

## Skill Version(s): <br>
2.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
