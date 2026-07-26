## Description: <br>
Generates Chinese-language product quality plan documents for general manufacturing products, covering quality objectives, control processes, inspection standards, risk assessment, CAPA, review planning, training, change management, supplier management, and Markdown or HTML export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality, manufacturing, and operations teams use this skill to collect product details, confirm a 12-module quality-plan outline, generate a tailored Markdown quality plan, and export a printable HTML version. It is intended for product quality planning, quality control方案, and quality management documentation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store sensitive product, customer, supplier, or process details in local quality-plan files. <br>
Mitigation: Use a dedicated output folder, apply appropriate access controls, and avoid including information the organization is not prepared to store locally. <br>
Risk: Generated file names or export paths could overwrite existing documents if reused carelessly. <br>
Mitigation: Use clear product-specific filenames and review target paths before creating or exporting documents. <br>
Risk: Quality-plan content may be incomplete or unsuitable if product requirements, standards, or acceptance criteria are missing. <br>
Mitigation: Have a qualified quality or manufacturing reviewer verify the final plan against applicable standards, customer requirements, and internal procedures before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-quality-plan) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-quality-plan) <br>
- [Quality plan outline reference](references/quality-plan-outline.md) <br>
- [Industry standards reference](references/industry-standards.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Conversational guidance, structured Markdown quality-plan content, and command examples for HTML export.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local Markdown and HTML files using user-provided product, customer, supplier, process, and quality information.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; source skill frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
