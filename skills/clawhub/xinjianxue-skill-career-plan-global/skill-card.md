## Description:

XinJianXue Career Planning Advisor helps an agent gather user-authorized personal details, call the XinJianXue API, and present career planning analysis grounded in the returned trait report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill through an agent to request personalized career direction and long-term path planning after confirming consent, completing XinJianXue account binding, and providing the required profile details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive personal details to XinJianXue and uses paid or free service tokens.

Mitigation: Use the skill only after explicit user consent, explain token consumption before calls, and avoid running the analysis for unapproved third parties.

Risk: The onboarding flow handles a one-time authorization code plus generated license and API credentials.

Mitigation: Store long-lived credentials only in a dedicated credential store or OS keychain, mask credential values in conversation, and rotate or contact support if exposure is suspected.

Risk: Returned reports may contain instruction-like language even though they are analysis material.

Mitigation: Treat report content as reference data only and follow the local skill role definition and user request when preparing the response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-career-plan-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API Calls, Configuration instructions]

**Output Format:** [Markdown guidance with optional HTTP request details and credential storage instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include translated career analysis from a time-sensitive XinJianXue report; requires user consent and valid dual credentials before API use.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
