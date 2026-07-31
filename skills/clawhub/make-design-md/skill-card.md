## Description: <br>
Analyzes website URLs, HTML files, or screenshots to extract design tokens and generate a Google design.md-compatible DESIGN.md document. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhouchang1988](https://clawhub.ai/user/zhouchang1988) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and designers use this skill to document a site's visual style as structured design tokens and human-readable design guidance. It supports analysis from public URLs, local HTML files, and screenshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated preview HTML may load Google Fonts through the third-party loli.net mirror. <br>
Mitigation: Review generated preview HTML before opening or sharing it, and replace or block external font loading when that mirror is not acceptable for the environment. <br>


## Reference(s): <br>
- [Google design.md specification](https://github.com/google-labs-code/design.md) <br>
- [DESIGN.md template](references/design-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [DESIGN.md with YAML front matter and Markdown body, plus optional HTML preview files and CLI command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated design documents follow the Google design.md section order and can be checked with the Google design.md CLI.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
