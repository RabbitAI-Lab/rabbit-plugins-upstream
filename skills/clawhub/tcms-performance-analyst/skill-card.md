## Description: <br>
Monthly content performance and output-analysis skill. Aggregates published content, the content calendar, channel-effect data, product-line coverage, and knowledge-base health; outputs a monthly report and next-cycle optimization suggestions. Does not auto-modify the schedule or trigger writing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Brand-side content and marketing teams use this skill to review monthly content output, compare planned versus actual publishing, inspect product-line coverage, and produce next-cycle recommendations from available project data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recommendations may be misapplied if the agent receives unrelated folders, incomplete metric files, or out-of-scope reporting requests. <br>
Mitigation: Provide only the intended calendar, published-content directory, product map, and metric files, then review the generated report before acting on recommendations. <br>
Risk: Missing channel-effect data can lead to overconfident performance interpretation. <br>
Mitigation: Require missing values to be marked DATA_MISSING and limit analysis to observable output dimensions when effect data is absent. <br>
Risk: Automated report suggestions could be mistaken for approved publishing-plan changes. <br>
Mitigation: Keep recommendations advisory and require human confirmation before calendar, priority, or downstream writing changes. <br>


## Reference(s): <br>
- [TCMS Performance Analyst on ClawHub](https://clawhub.ai/haiyangchenbj/skills/tcms-performance-analyst) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown monthly report saved as reports/YYYY-MM-monthly-report.md] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Marks missing performance data as DATA_MISSING and requires findings to cite dates, files, or data points.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
