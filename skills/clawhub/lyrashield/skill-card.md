## Description:

Review LyraShield release-assurance evidence through an OAuth-first MCP connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ecryptoguru](https://clawhub.ai/user/ecryptoguru)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release-assurance reviewers use this skill to inspect LyraShield evidence, summarize current issues, and explain pending approvals while preferring read-only interactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LyraShield API key and can perform write actions when the OAuth write scope is granted.

Mitigation: Provide LYRASHIELD_API_KEY only in appropriate release-assurance environments, prefer read-only use, and grant lyrashield.write only for deliberately approved write actions.

Risk: Release-assurance summaries could be mistaken for a complete security guarantee.

Mitigation: Treat the skill's output as review guidance and dashboard evidence summaries, not proof that every control or vulnerability was fully verified.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/ecryptoguru/skills/lyrashield)
- [Publisher profile](https://clawhub.ai/user/ecryptoguru)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference LyraShield dashboard evidence; read-only use is preferred and write actions require OAuth approval.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
