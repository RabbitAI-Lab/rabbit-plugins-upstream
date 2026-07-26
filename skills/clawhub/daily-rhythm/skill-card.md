## Description: <br>
Daily Rhythm automates morning briefs, wind-down prompts, sleep nudges, and weekly reviews for structured personal planning and reflection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anthonyfrancis](https://clawhub.ai/user/anthonyfrancis) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, founders, and professionals use this skill to configure automated daily planning routines, morning briefings, evening reflection prompts, and weekly review flows. It is especially useful when personal task, calendar, weather, and optional revenue signals need to be summarized into recurring planning outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Google Tasks and optional Stripe data through recurring automation and plaintext local storage. <br>
Mitigation: Enable only the integrations needed, use least-privilege Google and Stripe credentials, keep .env.stripe and OAuth token files out of version control, and treat generated memory files as sensitive. <br>
Risk: The included automation contains hard-coded workspace paths and cron-style recurring jobs. <br>
Mitigation: Edit the scripts to remove /Users/tom paths before use, verify each scheduled command, and add only cron jobs that can be audited and removed. <br>


## Reference(s): <br>
- [Daily Rhythm Configuration Guide](references/CONFIGURATION.md) <br>
- [Google Cloud Console](https://console.cloud.google.com/) <br>
- [Stripe API Keys Dashboard](https://dashboard.stripe.com/apikeys) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and local JSON state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces scheduled planning prompts, morning brief content, setup instructions, and local memory files for tasks, ARR, and routine state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
