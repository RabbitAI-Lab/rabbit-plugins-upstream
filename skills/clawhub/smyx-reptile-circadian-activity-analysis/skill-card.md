## Description: <br>
Analyzes fixed-camera reptile enclosure video to summarize 24-hour activity patterns, flag circadian rhythm disruption, and provide husbandry-oriented guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile keepers, breeders, researchers, and developers use this skill to analyze enclosure video or video URLs, produce circadian activity reports, review historical reports, and decide whether lighting or environmental conditions need follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud video analysis may send reptile enclosure media or video URLs to an external service. <br>
Mitigation: Use only footage appropriate for cloud processing, avoid sensitive shared-space media, and review the service relationship before use. <br>
Risk: The skill may automatically create or reuse an identity, query cloud report history, and persist backend tokens in a local workspace database. <br>
Mitigation: Prefer explicit account controls, avoid shared workspaces for sensitive reports, and clear the local database or stored tokens when access should end. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-circadian-activity-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown or JSON analysis report with activity summaries, alerts, recommended actions, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save report output to a user-specified file and may query cloud history for prior reports.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub release evidence; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
