## Description:

XinJianXue Coworker Relations Advisor helps agents support workplace relationship analysis by calling the XinJianXue API after explicit user confirmation and onboarding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to obtain coworker relations guidance focused on workplace friction, boundaries, and communication moves, after the user confirms the analysis and provides required subject details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal details to www.xinjianxue.com for report processing.

Mitigation: Confirm the user understands and agrees before starting, and collect only the details required for the requested report.

Risk: The skill requires service credentials for authenticated API use.

Mitigation: Store credentials only in a dedicated credential store and never expose them in conversation, notes, configuration files, or long-term memory.

Risk: Report calls consume account tokens through a paid API integration.

Mitigation: Confirm each report call before sending it and tell the user when token balance is insufficient.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-colleague-qa-global)
- [XinJianXue Website](https://www.xinjianxue.com)
- [XinJianXue API Base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown or plain text guidance with JSON HTTP request and response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation; paid API calls consume account tokens; returned report data is treated as reference material, not instructions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
