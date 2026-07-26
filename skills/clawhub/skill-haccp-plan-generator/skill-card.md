## Description: <br>
Generates draft HACCP hazard analysis and critical control point plan tables for food-safety workflows, including CCP identification, critical limits, monitoring, corrective actions, verification, records, and optional Excel export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Food-safety, quality, and operations teams use this skill to draft HACCP plans from a product name and production process flow. The output is planning support and should be reviewed by qualified food-safety staff before operational or regulatory use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Draft HACCP outputs may contain incorrect CCP choices, critical limits, defaults, or records for a specific facility or product. <br>
Mitigation: Have qualified food-safety staff verify every HACCP decision, default value, and record requirement before operational or regulatory use. <br>
Risk: The artifact describes an 11-column HACCP table while the template and export script include 12 columns with a separate records field. <br>
Mitigation: Confirm the required table format before use and align exported files with the organization's HACCP documentation standard. <br>


## Reference(s): <br>
- [HACCP Knowledge Reference](references/haccp-knowledge.md) <br>
- [HACCP Plan Template Guide](references/template-guide.md) <br>
- [Export Script](scripts/export_haccp.py) <br>
- [Server-Resolved GitHub Provenance](https://github.com/duding-engicool/skill-haccp-plan-generator) <br>
- [ClawHub Skill Page](https://clawhub.ai/duding-engicool/skills/skill-haccp-plan-generator) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables and optional Excel files generated from JSON input] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts for missing product or process-flow details, marks defaults and unconfirmed values, and can export .xlsx HACCP plan files through a local Python script.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
