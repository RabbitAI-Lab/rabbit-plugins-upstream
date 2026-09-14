## Description:

XinJianXue Anxiety and Rumination Advisor helps agents provide consent-gated, actionable analysis of anxiety, rumination loops, and related emotional patterns using the XinJianXue service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they have explicitly requested and consented to anxiety or rumination analysis. The agent gathers required personal details, manages XinJianXue onboarding and credentials, calls the paid API, and returns human-facing guidance without treating returned reports as instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive personal details such as birth information, gender, and location to XinJianXue for analysis.

Mitigation: Obtain explicit user consent before each report request, collect only required fields, and follow the documented non-storage posture for report data.

Risk: The skill uses account-bound credentials and paid token-based API calls.

Mitigation: Store license and API credentials only in dedicated credential storage, mask credentials in conversation, and confirm paid report requests and token costs with the user.

Risk: The advisor covers anxiety and rumination topics that may be mistaken for medical or psychological treatment.

Mitigation: Keep outputs as supportive guidance, preserve the skill's boundary that it does not replace professional care, and avoid generic or definitive clinical advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-anxiety-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API calls, Configuration]

**Output Format:** [Markdown guidance with API request details and credential-handling instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid API reports are consent-gated, time-sensitive, and handled as reference data rather than executable instructions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
