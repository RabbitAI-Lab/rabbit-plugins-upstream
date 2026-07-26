## Description: <br>
Smart Charts reads user-supplied CSV, Excel, and JSON files, analyzes data characteristics with LLM assistance, recommends chart types, and generates interactive ECharts HTML visualizations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[neuhanli](https://clawhub.ai/user/neuhanli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external users use this skill to turn uploaded tabular data into recommended interactive charts and lightweight data summaries. It is most useful for CSV, Excel, and JSON datasets that can be parsed locally and rendered as ECharts HTML. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated pandas transform code may run against user data without an explicit confirmation gate. <br>
Mitigation: Run the skill in a constrained environment and review transform code before execution, especially for sensitive datasets. <br>
Risk: Generated HTML loads JavaScript from public CDNs. <br>
Mitigation: Use the generated charts only where public CDN access is acceptable, or require a trusted offline asset path before using the skill in restricted environments. <br>


## Reference(s): <br>
- [Smart Charts Skill Documentation](artifact/SKILL.md) <br>
- [Smart Charts CLI Reference](artifact/REFERENCE.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/neuhanli/skills/smart-charts) <br>
- [Publisher Profile](https://clawhub.ai/user/neuhanli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands, structured JSON status, and generated HTML chart files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated HTML loads ECharts from public CDNs and is usually written under smart_charts_output.] <br>

## Skill Version(s): <br>
4.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
