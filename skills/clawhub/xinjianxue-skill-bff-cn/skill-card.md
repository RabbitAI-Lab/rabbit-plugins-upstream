## Description:

Provides a Chinese-language best-friend relationship advisor that, after explicit user confirmation and consent checks, calls the Xinjianxue API for a paid personal report and uses it as reference data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to get structured guidance about close friendship boundaries, comparison, competition, and perceived jealousy. The skill requires confirmation before analysis, collects profile details for the analysis subject, and treats returned reports as reference data rather than instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the user to paste a sensitive one-time account-binding authorization code into chat.

Mitigation: Tell the user the code is sensitive and one-time use, request it only for binding, and avoid storing or displaying it after use.

Risk: The skill stores account credentials for later API calls.

Mitigation: Store the license key and API key only in a dedicated secret store and do not write them into chat, notes, configuration files, or long-term model memory.

Risk: The skill transmits birth, gender, birthplace, and current location details to a third-party service for each consenting analysis subject.

Mitigation: Use the service only after explicit confirmation, confirm consent for each analyzed person, and disclose the transmitted data before starting.

Risk: Each report call spends account credits.

Mitigation: Explain the per-report credit cost before calling the report endpoint and handle insufficient-credit responses transparently.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-bff-cn)
- [Xinjianxue API service](https://chinaapi.xinjianxue.com)
- [Xinjianxue API path prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, API calls, configuration]

**Output Format:** [Markdown prose with HTTP request details and user-facing analysis guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a license key, API key, user confirmation, and consent for the analyzed person before report calls.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
