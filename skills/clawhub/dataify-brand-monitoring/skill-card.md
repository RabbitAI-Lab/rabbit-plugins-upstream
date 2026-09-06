## Description:

Monitor a brand across current news, search, reviews, forums, or public social sources and report material mentions, sentiment signals, and reputation risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to collect bounded public brand mentions, compare dated monitoring snapshots, identify sentiment signals, and surface reputation risks or coverage gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring runs can consume Dataify credits or expand beyond the intended scope.

Mitigation: Set a clear freshness window and max-action limit, use dry-run when appropriate, and confirm high-volume or multi-page scopes before execution.

Risk: The skill requires a Dataify API token for normal operation.

Mitigation: Configure the token in the local environment, verify only that it is present, and never print or expose token values in chat or output.

Risk: Dated monitoring snapshots may retain public mention data for later comparison.

Mitigation: Keep snapshots scoped to the monitoring purpose and review retained outputs for organizational data-handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-brand-monitoring)
- [Dataify account dashboard](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown monitoring snapshot with sourced findings and concise setup or execution guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dated evidence IDs, mention counts, channel mix, positive and negative signals, high-risk items, coverage gaps, and recommended response.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
