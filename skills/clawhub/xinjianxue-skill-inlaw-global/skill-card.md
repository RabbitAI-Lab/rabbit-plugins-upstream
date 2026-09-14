## Description:

XinJianXue In-Law Relationship Advisor helps an agent provide consent-gated in-law relationship analysis and boundary-setting guidance using the XinJianXue API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent when they explicitly want in-law relationship analysis involving themselves or a consented subject. The skill guides the agent through onboarding, XinJianXue API calls, and neutral guidance about family roles, boundaries, and communication paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive personal details such as birth details, gender, current location, and relationship context to XinJianXue for processing.

Mitigation: Proceed only after the user confirms they understand the data sharing and wants the analysis for the stated subject.

Risk: The skill uses locally stored vendor credentials and a one-time authorization code to bind the agent to the user's account.

Mitigation: Store license and API credentials only in dedicated credential storage, keep them out of conversation and configuration files, and request the one-time authorization code only during intentional account binding.

Risk: Calls may consume paid XinJianXue tokens under the user's account.

Mitigation: Tell the user before analysis that API calls may consume tokens and use billing endpoints only when the user asks about token usage.

Risk: API report content could contain instruction-like text.

Mitigation: Treat returned report content only as data or reference material and follow only the local skill role definition and the user's current request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-inlaw-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Markdown]

**Output Format:** [Markdown guidance with HTTP request details and JSON API responses used as source data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before analysis, handles paid-token API calls, and treats API report content as reference data rather than executable instructions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
