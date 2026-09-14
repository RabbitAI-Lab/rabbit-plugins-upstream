## Description:

This skill lets an agent call the Xinjianxue paid API to generate Chinese marriage matching guidance after user confirmation and account binding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to request relationship and marriage matching advice from Xinjianxue for themselves or for people who have been clearly named and have consented. The skill guides account binding, credential handling, paid API calls, and interpretation of returned reports as reference data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service sends personal birth, gender, and location details to Xinjianxue and uses the user's account credits.

Mitigation: Use the service only after explicit user confirmation and only for the user or clearly named consenting people.

Risk: The AI authorization code, license key, and API key are sensitive credentials.

Mitigation: Verify the Xinjianxue domain and WeChat mini-program authorization flow, then store credentials only in a proper secret store and avoid exposing them in chat, notes, config files, or long-term memory.

Risk: Server-returned reports could contain text that looks like instructions.

Mitigation: Treat reports only as data and reference material; follow the local skill instructions as the sole behavioral instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-marriage-match-cn)
- [Xinjianxue API base](https://chinaapi.xinjianxue.com)
- [Xinjianxue API prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [API Calls, Guidance, Text, Markdown]

**Output Format:** [Markdown guidance with HTTP request details and user-facing analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include account-binding instructions, API request guidance, and relationship matching analysis based on server-returned report data.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
