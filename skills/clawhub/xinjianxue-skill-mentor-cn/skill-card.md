## Description:

Provides a Chinese mentor-advice agent that, after user confirmation, calls the Xinjianxue paid HTTP API to produce guidance on mentor and senior-student relationships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to request guidance about working with mentors, supervisors, and senior peers. The agent gathers required consent and personal details, calls the Xinjianxue service, and turns the returned report into user-facing advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service sends sensitive birth, gender, birthplace, and current-location details to the provider.

Mitigation: Ask for explicit user confirmation before calling the service and disclose what personal data will be sent.

Risk: The skill uses a one-time authorization code plus saved license and API credentials.

Mitigation: Request the authorization code only during intentional account binding and store resulting credentials only in a proper secret store.

Risk: Calls consume account credits through a paid API integration.

Mitigation: Tell users that the service consumes credits before running the report and surface insufficient-credit responses plainly.

Risk: API-returned report content could contain instruction-like text.

Mitigation: Treat returned reports only as reference data and follow the local skill role for instructions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-mentor-cn)
- [Publisher Profile](https://clawhub.ai/user/weixin97676414)
- [Xinjianxue API Base](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, API Calls]

**Output Format:** [Markdown prose with API-derived report analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before use and treats returned reports as reference data, not executable instructions.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
