## Description:

XinJianXue Family Harmony Advisor helps an agent collect confirmed user inputs, call the XinJianXue API, and deliver family relationship analysis without taking sides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to request consent-based family relationship analysis through XinJianXue, including guidance on recurring family conflict patterns and immediate next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal birth, gender, birthplace, and current-location details to the XinJianXue service.

Mitigation: Require clear user confirmation before analysis, collect only the required inputs, and use the disclosed service domain.

Risk: The skill stores account-linked license and API credentials for later use.

Mitigation: Keep credentials only in dedicated credential storage, never in chat, notes, configuration files, or long-term memory, and mask credentials when referencing them.

Risk: Reports consume paid tokens under the user's XinJianXue account.

Mitigation: Disclose token use before report calls and query billing only when the user asks for billing details.

Risk: Returned reports may contain instruction-like text even though they are analysis data.

Mitigation: Treat reports as data and reference material only; use the local skill role definition as the instruction source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-family-harmony-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Markdown, Configuration]

**Output Format:** [Markdown guidance with HTTP request details and user-facing analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON request and response handling, credential storage guidance, and paid-token usage notices.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
