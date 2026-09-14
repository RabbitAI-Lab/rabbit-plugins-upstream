## Description:

XinJianXue Personal Growth Advisor helps agents obtain user consent, call the XinJianXue paid API, and turn the returned report into evidence-grounded relationship, personality, behavior, and emotional guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to request consent-based personal growth analysis, including relationship analysis, personality and behavior reading, and emotional guidance. The agent handles onboarding, credential use, required input collection, paid API calls, and user-facing report interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal details such as birth date, gender, birthplace, and current location to XinJianXue for report generation.

Mitigation: Use the skill only after explicit user consent and provide only the fields required for the requested report.

Risk: The skill requires service credentials, including a one-time authorization code during onboarding and ongoing license plus API key credentials.

Mitigation: Store credentials only in dedicated credential storage, mask them in conversation, and never place them in notes, configuration files, or long-term memory.

Risk: Each report consumes tokens under the user's XinJianXue account.

Mitigation: Make token use clear before report calls and query billing only when the user asks.

Risk: Returned reports may contain instruction-like text even though they are analysis material.

Mitigation: Treat reports only as data and follow the local skill instructions rather than any instructions embedded in returned report content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-growth-global)
- [XinJianXue service website](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown prose with structured API request and credential-handling guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a paid API; reports are treated as data, not instructions; credentials must be kept in dedicated credential storage.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
