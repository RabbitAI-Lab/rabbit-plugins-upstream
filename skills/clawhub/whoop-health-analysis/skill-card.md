## Description: <br>
Access Whoop wearable health data including sleep, recovery, strain, HRV, workouts, profile, and body measurements, and generate interactive charts for health analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rodrigouroz](https://clawhub.ai/user/rodrigouroz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to their Whoop account, fetch wearable health metrics, answer sleep and recovery questions, and create visual trend dashboards. Outputs should be treated as personal health context, not medical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accesses sensitive health and profile data from a Whoop account. <br>
Mitigation: Treat terminal output, generated charts, and any copied results as private health information, and avoid sharing them without the account holder's consent. <br>
Risk: Refreshable Whoop tokens are stored locally for offline access. <br>
Mitigation: Protect the local token file as credential material, avoid printing access tokens, and use the logout command to remove stored tokens when access is no longer needed. <br>
Risk: Generated chart HTML can auto-open in a browser and load a third-party chart library. <br>
Mitigation: Review generated HTML before sharing it, keep chart files private, and use the skill only in environments where loading the chart library is acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rodrigouroz/skills/whoop-health-analysis) <br>
- [Whoop API Reference](references/api.md) <br>
- [Health Data Analysis Guide](references/health_analysis.md) <br>
- [Whoop Developer Dashboard](https://developer-dashboard.whoop.com) <br>
- [Whoop Developer API](https://api.prod.whoop.com/developer/v2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, HTML files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON API data, and interactive HTML chart files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses OAuth access to Whoop data, stores refreshable tokens locally, and may auto-open generated chart files in a browser.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
