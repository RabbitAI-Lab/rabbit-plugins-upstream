## Description: <br>
Generate a daily health brief from Oura, Whoop, and Withings. Unified re-auth script, local token persistence, Green/Yellow/Red morning summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nathanielweiner](https://clawhub.ai/user/nathanielweiner) <br>

### License/Terms of Use: <br>


## Use Case: <br>
OpenClaw users and developers use this skill to fetch health metrics from WHOOP, Oura, and Withings, normalize them into a stable daily schema, and generate a concise morning health brief for review or automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles long-lived health account tokens for WHOOP, Oura, and Withings. <br>
Mitigation: Use a dedicated least-privilege 1Password vault or narrowly scoped environment variables, keep local token files private, and avoid broad secrets files in scheduled jobs. <br>
Risk: The documented main CLI and reauthorization scripts are missing from the package. <br>
Mitigation: Review the installed package and ask the publisher to include the missing scripts before entering provider credentials or enabling automation. <br>
Risk: Health JSON written to shared temporary paths can expose sensitive personal metrics. <br>
Mitigation: Write outputs to a private user-controlled directory rather than /tmp, and restrict file permissions where possible. <br>
Risk: The skill performs live API calls when credentials are present. <br>
Mitigation: Confirm OAuth scopes and provider permissions before use, and inspect generated summaries before forwarding them to external channels. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nathanielweiner/skills/openclaw-health-brief) <br>
- [Morning brief documentation](docs/MORNING_BRIEF.md) <br>
- [1Password conventions](docs/1PASSWORD_CONVENTIONS.md) <br>
- [WHOOP connector notes](docs/WHOOP.md) <br>
- [Oura connector notes](docs/OURA.md) <br>
- [Withings connector notes](docs/WITHINGS.md) <br>
- [OpenClaw cron documentation](https://docs.openclaw.ai/automation/cron) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Normalized JSON files and concise Markdown health summaries, with setup and automation commands in documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provider-specific metrics may be null when credentials are absent or data is unavailable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
