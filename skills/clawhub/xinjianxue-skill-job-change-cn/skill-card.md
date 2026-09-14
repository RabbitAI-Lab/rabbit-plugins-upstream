## Description:

心鉴学「跳槽选择指导顾问」技能包 helps an agent call the 心鉴学 service, with user confirmation, to provide career change and offer-selection guidance based on a paid third-party report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they explicitly want the 心鉴学 job-change advisor to weigh career change, offer selection, or transition questions. The agent gathers consent and required profile details, calls the third-party report API, and returns a balanced decision framework rather than an absolute decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends detailed personal profile data, including birth time, gender, birthplace, and current location, to a third-party service.

Mitigation: Confirm the exact fields, analysis subject consent, destination service, and report charge before each report request.

Risk: The skill uses account-bound API credentials and a one-time authorization code during setup.

Mitigation: Store license and API credentials only in dedicated secret storage, mask them in conversation, and never ask the user for the API key itself.

Risk: The service can be misused to analyze a third party who has not agreed to the analysis.

Mitigation: Use the report only for the user or for a clearly identified person whose consent the user confirms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-job-change-cn)
- [心鉴学 API base](https://chinaapi.xinjianxue.com)
- [心鉴学 API path prefix](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Markdown or plain text career guidance informed by JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before paid report calls; returned reports are treated as reference data, not instructions.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
