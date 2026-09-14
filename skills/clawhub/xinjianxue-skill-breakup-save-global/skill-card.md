## Description:

Helps an agent deliver XinJianXue breakup recovery and reconciliation guidance by collecting consented relationship inputs, calling the XinJianXue report API, and turning the returned report into user-facing advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to request breakup recovery and reconciliation analysis after confirming the service is wanted and the subject has agreed to be analyzed. The skill guides account onboarding, consent checks, required personal inputs, and delivery of practical relationship guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive birth, gender, birthplace, and current-location details to a paid third-party service.

Mitigation: Ask for explicit confirmation before analysis, analyze only the user or a clearly agreed subject, and disclose the data transfer and token cost before calling the service.

Risk: The skill manages persistent account credentials for the user's XinJianXue account.

Mitigation: Store license and API credentials only in dedicated credential storage such as an OS keychain or managed secret store, never in chat, configuration files, or long-term memory.

Risk: Report calls consume paid tokens under the user's account.

Mitigation: Call the report endpoint only after the user clearly requests and confirms the analysis, and explain token insufficiency or billing results only when relevant.

Risk: Returned reports may contain instruction-like wording even though they are analysis data.

Mitigation: Treat returned reports only as reference material and follow the local skill role definition as the instruction source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-breakup-save-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text guidance with JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated XinJianXue API calls; reports are treated as reference data and not stored by the skill.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
