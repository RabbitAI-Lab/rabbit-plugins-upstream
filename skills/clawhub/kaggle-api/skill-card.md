## Description:

Helps agents access Kaggle datasets, models, competitions, and notebooks through Maton-managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Kaggle users can search and access datasets, models, competitions, and notebooks using their authorized Kaggle connection. The skill also describes optional, user-approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad account access or exposure of a long-lived API key.

Mitigation: Prefer OAuth with only the required scopes; avoid raw MATON_API_KEY use unless necessary.

Risk: Writes or persistent automation may modify data or forward events without ongoing review.

Mitigation: Confirm the specific write, function, trigger, and destination with the user before enabling them; review any forwarding destination separately.

## Reference(s):

- [Kaggle API documentation](https://www.kaggle.com/docs/api)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)
- [Kaggle skill release](https://clawhub.ai/maton/skills/kaggle-api)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton account and Kaggle connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
