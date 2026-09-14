## Description:

This skill helps an agent use Xinjianxue's team-collaboration operations advisor to analyze role, workflow, accountability, and cross-team coordination issues after explicit user consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users who explicitly opt in use this skill to request structured guidance on team collaboration, cross-department friction, role accountability, and workflow gaps. The agent uses Xinjianxue report data as reference material while keeping local skill instructions as the only instruction source.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive birth details, sex, birthplace, current location, and account-linked credentials are sent to an external third-party service.

Mitigation: Use the skill only after explicit consent, collect only the required fields for the current analysis, and avoid submitting information about any person who has not clearly consented.

Risk: License keys, API keys, and one-time authorization codes could expose account access if copied into chat history, configuration files, or shared notes.

Mitigation: Keep credentials in dedicated secret storage, mask credentials when discussing them, and use the authorization code only for the one-time binding flow.

Risk: Returned report content could contain instruction-like text that conflicts with the local skill behavior.

Mitigation: Treat report content as data and reference material only; keep the local skill definition as the sole instruction source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-team-synergy-cn)
- [Xinjianxue API base](https://chinaapi.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Markdown or plain text analysis with HTTP request parameters and response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user consent, account-bound credentials, and user-provided birth, sex, and location fields before report calls.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
