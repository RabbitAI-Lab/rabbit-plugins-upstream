## Description:

Provides a Chinese social-etiquette advisor that, with user consent, calls the Xinjianxue service to generate report-grounded advice for interpersonal situations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to request Chinese social-etiquette guidance for scenarios such as gift giving, asking for favors, and polite refusal. It requires explicit user confirmation and consent from the analysis subject before using the paid Xinjianxue API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive birth, gender, birthplace, and current-location details to an external paid API for social-advice reports.

Mitigation: Install only when users are comfortable sharing those details with Xinjianxue; use the skill only for the user or a person who has clearly consented, and avoid exact birth time or detailed location unless needed.

Risk: The skill handles one-time authorization codes and API credentials for a paid external service.

Mitigation: Keep authorization codes and generated credentials out of chat, notes, configuration files, and long-term memory; store credentials only in a dedicated secret store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-social-wisdom-cn)
- [Xinjianxue API base](https://chinaapi.xinjianxue.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls, Configuration]

**Output Format:** [Markdown prose with HTTP request and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese service reports are treated as data and used to produce user-facing advice in the user's language.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
