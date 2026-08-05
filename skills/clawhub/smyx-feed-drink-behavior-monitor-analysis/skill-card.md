## Description: <br>
Analyzes fixed-camera videos of feeders and waterers to quantify livestock feeding duration, feeding bouts, and drinking frequency, comparing them against individual baselines to raise behavior anomaly alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agricultural operations use this skill to analyze fixed-camera livestock feeder or waterer images and videos for feeding duration, feeding bouts, drinking frequency, baseline deviations, and anomaly alerts. It also supports querying historical behavior monitoring reports from the configured service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Livestock images or videos, media URLs, generated identity values, and report queries are sent to configured lifeemergence.com services. <br>
Mitigation: Use only media and URLs that the operator is authorized to send to the configured service, and avoid private or internal URLs unless the backend fetch path is trusted. <br>
Risk: The local workspace data directory may contain a SQLite database with user records and service tokens. <br>
Mitigation: Treat the workspace data directory as sensitive, restrict access to it, and clean stored state when the skill is no longer needed. <br>
Risk: The skill produces behavior statistics and anomaly alerts, not veterinary diagnosis or treatment guidance. <br>
Mitigation: Use outputs as decision-support data and confirm feeding, health, or treatment actions through farm procedures and qualified professionals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-feed-drink-behavior-monitor-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [畜禽采食/饮水行为监测 API 接口文档](references/api_doc.md) <br>
- [Common Analysis API 接口文档](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Text, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown or JSON text, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include structured behavior metrics, anomaly levels, historical report lists, and report links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
