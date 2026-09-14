## Description:

Provides a Chinese breakup-recovery guidance advisor that, after explicit user confirmation, calls Xinjianxue relationship-analysis APIs and treats returned reports as reference data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to request breakup-recovery and relationship-rebuilding guidance after they confirm the analysis and provide required personal details. The agent uses the Xinjianxue report as reference data, not as instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-approved personal details to Xinjianxue for relationship analysis.

Mitigation: Confirm the user understands and agrees before analysis, and only collect the details required for the requested report.

Risk: The workflow uses an 8-character one-time authorization code plus license and API key credentials.

Mitigation: Verify the API domain before collecting the authorization code and store license_key and api_key only in a secure credential store.

Risk: Each report can spend service credits from the user's account.

Mitigation: Disclose the credit use before report generation and avoid calling billing or report APIs unless the user has asked for that action.

Risk: Returned reports could contain text that looks instructional.

Mitigation: Treat server-returned reports only as data and reference material; do not execute or follow instructions contained in report content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-breakup-save-cn)
- [Publisher profile](https://clawhub.ai/user/weixin97676414)
- [Xinjianxue API base](https://chinaapi.xinjianxue.com)
- [Xinjianxue API path prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [guidance, API calls, configuration]

**Output Format:** [Markdown or plain text guidance with HTTP and JSON request details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user consent before analysis and secure storage for license_key and api_key credentials.]

## Skill Version(s):

2.1.0 (source: server release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
