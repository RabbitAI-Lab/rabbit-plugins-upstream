## Description: <br>
Generate a daily health brief from Oura, Whoop, and Withings. Unified re-auth script, local token persistence, Green/Yellow/Red morning summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nathanielweiner](https://clawhub.ai/user/nathanielweiner) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to fetch daily health metrics from supported wearable providers, normalize them into a stable JSON schema, and produce a concise Markdown morning brief. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive health metrics from wearable providers. <br>
Mitigation: Install only if you are comfortable granting access to those metrics, store generated output outside shared or temporary paths, and share only the intended summary. <br>
Risk: The skill uses OAuth refresh tokens and can persist rotated tokens locally or in 1Password. <br>
Mitigation: Prefer a dedicated 1Password vault or service account limited to the OpenClaw health items, check local token file permissions, and revoke provider tokens if you stop using the skill. <br>
Risk: Scheduled automation can expose more credentials than the health brief requires. <br>
Mitigation: Avoid sourcing broad secrets files in cron jobs and scope environment variables or vault access to the three supported provider credentials. <br>


## Reference(s): <br>
- [OpenClaw Health Skill Page](https://clawhub.ai/nathanielweiner/skills/openclaw-health) <br>
- [README](README.md) <br>
- [1Password Conventions](docs/1PASSWORD_CONVENTIONS.md) <br>
- [Morning Brief Format](docs/MORNING_BRIEF.md) <br>
- [Oura Connector Notes](docs/OURA.md) <br>
- [WHOOP Connector Notes](docs/WHOOP.md) <br>
- [Withings Connector Notes](docs/WITHINGS.md) <br>
- [OpenClaw Cron Documentation](https://docs.openclaw.ai/automation/cron) <br>
- [WHOOP Developer Portal](https://developer.whoop.com) <br>
- [Oura API Documentation](https://cloud.ouraring.com/v2/docs) <br>
- [Withings Developer Portal](https://developer.withings.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [JSON file plus Markdown summary and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include null metrics or provider error blocks when credentials or data are unavailable.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
