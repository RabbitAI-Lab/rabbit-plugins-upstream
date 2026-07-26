## Description: <br>
Analyzes fixed-camera home video or image inputs for behavior signals such as dazing, sighing, and self-talking, then returns behavior statistics, an emotional-risk level, recommendations, and report links without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users such as family members, care providers, and community workers can use this skill to analyze solo-living elder activity-area footage for non-diagnostic behavioral risk indicators and care prompts. Developers and agents can also use it to request current or historical structured reports from the configured cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive elder home video, video URLs, derived reports, report history, and account identifiers may be sent to Lifeemergence cloud endpoints. <br>
Mitigation: Use the skill only with informed consent from the monitored elder or lawful guardian, confirm cloud data handling and retention terms before use, and avoid submitting footage beyond the minimum needed for care review. <br>
Risk: Reports are associated with a persisted local identity and stored tokens. <br>
Mitigation: Restrict workspace access, review how the local database and token files are protected, and rotate or remove credentials when the workspace changes owners or is no longer needed. <br>
Risk: Exported report links and historical report queries may expose sensitive health-related observations. <br>
Mitigation: Verify who can access report links, limit sharing to authorized caregivers, and remove or expire exported reports according to the deployment's privacy policy. <br>
Risk: Behavioral signals may be mistaken for clinical depression indicators. <br>
Mitigation: Treat outputs as non-diagnostic behavioral prompts and route medical concerns to qualified clinicians or emergency services when appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Structured JSON or Markdown text with behavior metrics, risk level, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include exported report-image URLs and historical report records returned by cloud APIs.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
