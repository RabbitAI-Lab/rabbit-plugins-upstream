## Description: <br>
Generates a management daily dashboard HTML report from paginated recording AI summaries, using LLM analysis to organize team assets, field efficiency, compliance monitoring, RM ranking, lead conversion, and management advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operational managers and agent users use this skill to turn recording-derived AI summaries into a daily management dashboard report. The workflow supports normal and empty-data reporting while returning a generated report path to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive recording-derived business summaries. <br>
Mitigation: Confirm LLM handling, retention, and access policies are acceptable before deployment. <br>
Risk: Generated HTML reports are persisted and may expose sensitive management data if stored broadly. <br>
Mitigation: Store reports only in access-controlled locations and apply normal retention controls. <br>
Risk: Report generation may introduce script-execution or content-injection exposure. <br>
Mitigation: Ensure generated text is HTML-escaped or sanitized and that Chart.js is bundled or pinned with integrity controls. <br>
Risk: Recording API access may be incorrectly scoped beyond the current session. <br>
Mitigation: Confirm API requests are scoped to the resolved current-session agent before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/management-dashboard-skill) <br>
- [Publisher profile](https://clawhub.ai/user/legionspace-hackathon) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, HTML files, JSON status] <br>
**Output Format:** [Text response with generated HTML report path and structured JSON status from the script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Persists generated reports under the skill reports directory; empty data still produces an HTML report.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
