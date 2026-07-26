## Description: <br>
Track hours saved and calculate ROI with category-based rates to measure and prove the value an AI assistant generates over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sergirostoll-coder](https://clawhub.ai/user/sergirostoll-coder) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and business users use this skill to log AI-assisted tasks, estimate hours saved, apply category-based hourly rates, and produce summaries or reports that show assistant-generated value. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled sample data can affect summaries and reports if used unchanged. <br>
Mitigation: Review or clear data.json before first use when reports should reflect only the user's own work. <br>
Risk: Logged task descriptions, notes, Markdown reports, or JSON exports may contain sensitive business details. <br>
Mitigation: Avoid logging secrets or highly sensitive details, and review reports or exports before sharing them. <br>


## Reference(s): <br>
- [Value Tracker on ClawHub](https://clawhub.ai/sergirostoll-coder/skills/value-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Terminal text, Markdown reports, and JSON exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores task entries locally in data.json and reads rates and currency settings from config.json.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
