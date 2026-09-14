## Description:

XinJianXue Friendship & Social Advisor helps an agent provide consent-based friendship and social relationship guidance using the XinJianXue API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to request friendship-focused relationship analysis and practical social guidance after explicit consent. The skill is intended for everyday friendship questions, not for unsupported third-party profiling or decisions to end relationships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive relationship-analysis inputs and birth or location details to www.xinjianxue.com.

Mitigation: Require explicit user confirmation before calls, disclose the data transfer, and send only the fields needed for the requested analysis.

Risk: The skill uses a one-time authorization code, generated license credentials, API credentials, and paid service tokens.

Mitigation: Request the authorization code only for account binding, store generated credentials in dedicated credential storage, mask secrets in conversation, and disclose token usage before report calls.

Risk: Returned reports may contain instruction-like text even though they are analysis material.

Mitigation: Treat API reports as reference data only and rely on the local skill role definition for operational instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-friend-qa-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [text, guidance, API calls, configuration]

**Output Format:** [Markdown or plain text with JSON HTTP request and response handling as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation, HTTP access, dedicated credential storage, and sufficient paid service tokens before report calls.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
