## Description:

XinJianXue Job-Change Decision Advisor helps an agent support consented career transition questions by calling the XinJianXue API for trait-based reports and translating them into a balanced stay-or-leave framework.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill when the user has explicitly requested help with a job change, offer comparison, or career transition decision. The skill provides an onboarding flow for the paid XinJianXue API, collects required personal details with consent, and turns the returned report into balanced career guidance rather than an absolute decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal details such as birth date, gender, birthplace, and current location to a paid external API.

Mitigation: Confirm the user understands and agrees before use, and share only the required fields with www.xinjianxue.com.

Risk: The skill uses a one-time authorization code and stores license and API credentials for later calls.

Mitigation: Use only the official authorization flow, and store credentials in a trusted credential store rather than chat, notes, configuration files, or long-term memory.

Risk: Returned reports may contain instruction-like text even though they are analysis material.

Mitigation: Treat service reports only as data or reference material and rely on the local skill role definition for instructions.

## Reference(s):

- [XinJianXue service site](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)
- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-job-change-global)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration guidance]

**Output Format:** [Markdown guidance with JSON request examples and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report-based career guidance, credential storage guidance, billing status summaries, and masked credential references.]

## Skill Version(s):

1.0.0 (source: server release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
