## Description: <br>
Analyzes fixed-camera workplace video or video URLs to produce anonymous, zone-level group stress indices, heatmap colors, trend summaries, and manager-facing recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Workplace health, facilities, and operations teams use this skill to analyze office-area camera footage and review aggregate stress distribution by workstation zone. It is intended for organizational health monitoring and environment optimization, not individual employee identification, diagnosis, or performance evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive employee camera footage or video URLs through cloud APIs and may create or reuse persistent operator identity and token state. <br>
Mitigation: Before installation, confirm employee notice and consent, an approved workplace-camera stress-inference policy, explicit approval for sending video or video URLs plus operator identifiers to lifeemergence.com services, and reviewed retention, access control, and token storage expectations. <br>
Risk: Stress heatmap outputs could be misused as individual performance-management evidence or psychological diagnosis. <br>
Mitigation: Treat outputs as sensitive organizational health data, limit use to aggregate workplace-health monitoring, and prohibit individual identification, diagnosis, or performance evaluation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON containing structured stress-analysis results, heatmap/report links, and historical report listings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended to be aggregate and zone-level; areas with fewer than three people are documented as insufficient sample cases.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
