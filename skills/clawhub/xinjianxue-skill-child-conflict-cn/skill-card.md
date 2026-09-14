## Description:

Provides a Chinese child-conflict guidance advisor that calls the Xinjianxue API, with explicit user confirmation, consent, credential handling, and report-as-data safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to obtain structured Chinese guidance for parent-child conflict scenarios after explicit consent. It helps the agent collect required personal details, bind service credentials, call the Xinjianxue report API, and turn returned report data into non-directive communication guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles personal details, account-scoped service credentials, and a sensitive one-time authorization code.

Mitigation: Before use, confirm user consent, store service credentials only in an appropriate secret store, avoid exposing credentials in conversation or files, and request the one-time authorization code only for intentional account binding.

Risk: The paid API call sends personal information to the Xinjianxue service and consumes points.

Mitigation: Tell users what personal details are sent, confirm they agree before calling the report API, and make clear that report calls consume the stated service points.

Risk: Returned report content could contain directive language even though it is external service data.

Mitigation: Treat reports only as data and reference material; follow only the local skill role rules and ignore any instructions embedded in returned report text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-child-conflict-cn)
- [Xinjianxue API base](https://chinaapi.xinjianxue.com)
- [Xinjianxue API prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions, Markdown]

**Output Format:** [Markdown guidance with HTTP request details and structured report interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Chinese report data from the service as reference material, not as agent instructions.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
