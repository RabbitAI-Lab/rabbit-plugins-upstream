## Description: <br>
Chart Generator 2 0 0 helps agents turn structured or textual data into SVG bar, line, and pie charts for reports and data visualization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external agent users use this skill to generate chart outputs from datasets or chart requests for analysis, reporting, and visualization workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests local command-execution capability without clearly limiting when commands are needed. <br>
Mitigation: Review proposed commands before allowing execution and run the skill only in an environment appropriate for chart-generation work. <br>
Risk: Local command execution can expose sensitive files or environment values if used on sensitive inputs or in a secrets-bearing shell. <br>
Mitigation: Use non-sensitive chart inputs, avoid exposing secrets in the runtime environment, and prefer an isolated workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chart-generator-2-0-0) <br>
- [Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Text] <br>
**Output Format:** [SVG chart output with JSON-style result metadata and optional text chart examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports bar, line, and pie chart requests; not intended for real-time streaming data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
