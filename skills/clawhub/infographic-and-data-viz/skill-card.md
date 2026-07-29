## Description: <br>
Helps agents turn real, sourced data into honest, accessible chart and infographic specifications using the CHART framework. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, content, and analytics teams use this skill to convert real business findings into publishable social charts, infographics, and data-visualization briefs. It emphasizes chart choice, takeaway titles, honest scales, source/date tagging, accessibility, and human approval before publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to use real business or analytics data, which may include sensitive or confidential information. <br>
Mitigation: Review datasets and intended chart content before use, redact sensitive data, and require source/date tagging for all visualized claims. <br>
Risk: Poor chart choices, distorted scales, cherry-picked ranges, or fabricated data could mislead readers. <br>
Mitigation: Apply the CHART checks before rendering: choose an appropriate chart, use takeaway titles, keep bar scales zero-based, avoid 3D and dual-axis distortion, show relevant context, and reject fabricated or unsourced data. <br>
Risk: External design or publishing workflows may render or distribute visuals beyond the agent's direct control. <br>
Mitigation: Use the agent output as a specification, have a design or chart tool render the final asset, and require human approval before publication. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/social-media-skills/skills/infographic-and-data-viz) <br>
- [The CHART Framework](references/the-chart-framework.md) <br>
- [Chart Picker, Checklists & Worked Examples](references/chart-picker-and-templates.md) <br>
- [Scope, Distinctions & Connections](references/scope-and-connections.md) <br>
- [The Reality of Data Viz & Infographics in 2026](references/infographic-and-data-viz-2026-reality.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance and structured visualization specifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include chart type, takeaway headline, data requirements, scale rules, labels, color and accessibility guidance, alt text, source/date notes, and publication handoff guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
