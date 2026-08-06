## Description: <br>
Ppshu Github helps agents create self-contained HTML diagrams, visual explanations, interactive prototypes, and diff reports saved into a local .ppshu gallery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ppshux](https://clawhub.ai/user/ppshux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and other agent users use this skill to turn concepts, workflows, architectures, state machines, interactive UI ideas, and file comparisons into offline HTML visualizations or review reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates local HTML and JavaScript files in the current project. <br>
Mitigation: Use the default .ppshu output folder when possible and review generated files before relying on or sharing them. <br>
Risk: Diff reports can read files selected for comparison and embed source text in generated HTML. <br>
Mitigation: Compare only intended files and review generated reports before sharing them outside the workspace. <br>
Risk: Overriding PPSHU_DIR or passing --dir can write generated output outside the default project gallery. <br>
Mitigation: Avoid pointing output overrides at sensitive locations unless the broader write location is intentional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ppshux/skills/ppshu) <br>
- [Publisher profile](https://clawhub.ai/user/ppshux) <br>
- [README](artifact/README.md) <br>
- [HTML cookbook](artifact/references/html_cookbook.md) <br>
- [Mermaid flowchart template](artifact/references/mermaid_flowchart_template.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTML, JavaScript, and shell command snippets; generated artifacts are standalone HTML files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated HTML is stored locally in .ppshu by default; diff reports may embed source text and SHA-256 hashes.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release metadata and artifact manifest.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
