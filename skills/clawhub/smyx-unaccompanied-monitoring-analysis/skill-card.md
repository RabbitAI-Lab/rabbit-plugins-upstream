## Description: <br>
Determines when elderly people living alone have no interaction or visitors for extended periods, and actively pushes care reminders to family members, suitable for remote care scenarios for elderly people living alone at home. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Care teams, family caregivers, and agents supporting elder-care workflows use this skill to analyze home monitoring images, videos, or URLs for extended periods without interaction or visitors and to retrieve related cloud report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private elder-care photos, videos, or supplied URLs are sent to LifeEmergence cloud services for analysis. <br>
Mitigation: Use only with explicit consent from monitored people and caregivers, and verify the provider's data handling, retention, and access policies before deployment. <br>
Risk: Cloud report history can be queried and may reveal sensitive home-care monitoring records. <br>
Mitigation: Limit installation and use to trusted agents and accounts with a legitimate care workflow need, and review access controls for report history before enabling the skill. <br>
Risk: The skill may silently create or reuse an identity and store tokens locally. <br>
Mitigation: Avoid use where account binding must be explicitly confirmed by the user, and review local token storage and identity reuse behavior before production use. <br>
Risk: Analysis results are care reminders and may be incomplete or inaccurate. <br>
Mitigation: Treat outputs as decision support only and require human follow-up for elder safety, urgent care, or professional nursing decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Unaccompanied monitoring API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON text with structured analysis results, report-list output, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can optionally write the returned report text to a local output file.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
