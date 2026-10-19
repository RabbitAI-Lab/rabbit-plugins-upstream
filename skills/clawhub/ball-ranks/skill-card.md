## Description:

Helps agents answer fantasy NFL and NBA questions with Ball Ranks rankings and projections, including weekly football start/sit comparisons and season draft boards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ollynov](https://clawhub.ai/user/ollynov)

### License/Terms of Use:

MIT-0

## Use Case:

Fantasy sports players and their agents use this skill to compare NFL start/sit options, explore NFL and NBA draft rankings, and look up player projections with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Questions sent to Ball Ranks leave the agent's environment.

Mitigation: Use the service only for intended fantasy sports queries and avoid sending sensitive information.

Risk: Anonymous requests are rate-limited, so rankings may be unavailable after the limit is reached.

Mitigation: Keep requests focused and report unavailable results rather than inventing rankings.

Risk: A supplied premium API key could be exposed or sent to another service.

Mitigation: Send the key only to Ball Ranks, and keep it out of URLs, logs, and answers.

## Reference(s):

- [Ball Ranks developer documentation](https://ballranks.com/developers)
- [Ball Ranks API schema](https://ballranks.com/openapi.json)
- [Ball Ranks ClawHub listing](https://clawhub.ai/ollynov/skills/ball-ranks)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers identify relevant ranking or projection scope, model and source link when available.]

## Skill Version(s):

1.0.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
