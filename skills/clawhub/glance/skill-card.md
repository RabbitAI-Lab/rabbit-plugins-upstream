## Description: <br>
Create, update, and manage Glance dashboard widgets for visualizing metrics, API data, and monitored information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[acfranzen](https://clawhub.ai/user/acfranzen) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and AI agent operators use Glance to create, arrange, refresh, and inspect local dashboard widgets that visualize API data, CLI outputs, credentials-backed service data, and status summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can grant an agent ongoing authority through scheduled refresh jobs and local command or CLI use. <br>
Mitigation: Enable refresh schedules only after reviewing the widget's fetch.instructions and confirming the commands are necessary. <br>
Risk: The dashboard may store credentials and use them for widgets that access external services. <br>
Mitigation: Use least-privilege, revocable tokens and keep Glance local or protected by strong authentication. <br>
Risk: Imported widgets and widget instructions can influence what data an agent collects and posts to the dashboard. <br>
Mitigation: Review imported widget definitions and fetch.instructions before enabling refreshes or credential-backed behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/acfranzen/skills/glance) <br>
- [Glance GitHub Repository](https://github.com/acfranzen/glance) <br>
- [Glance README](artifact/README.md) <br>
- [Widget SDK Documentation](artifact/widget-sdk.md) <br>
- [Dashboard Management API](artifact/dashboard-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON, HTTP, shell, and JSX/TSX code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GLANCE_URL and curl; may create or update dashboard widgets, credentials, cache entries, and refresh schedules.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
