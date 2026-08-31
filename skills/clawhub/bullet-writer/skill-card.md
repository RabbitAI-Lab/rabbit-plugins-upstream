## Description:

Combines Amazon product details and review evidence to diagnose gaps in bullet-point selling points, customer questions, and wording, then provides bullet optimization guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to run a fixed listing/bullets workflow and turn product details plus review evidence into bullet-point optimization recommendations. It is not intended for title rewriting, advertising keyword or bid management, or automatic Amazon listing publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is advertised as a narrow Amazon bullet-point optimization helper, but the security evidence says it also ships and documents broader ARI account operations, including paid actions, monitoring changes, exports, and remote state updates.

Mitigation: Install only when the user intends to grant broad ARI account access; review the command scope, account permissions, export behavior, scheduled monitoring, watch actions, competitor actions, and any paid-command confirmation flow before use.

Risk: Paid collection, analysis, leaderboard, operations, and advice commands can affect credits or account state if confirmed without review.

Mitigation: Require the free quote or preview first, preserve and reuse the quoted requestId where applicable, and execute commands with --confirm only after explicit user authorization.

Risk: The skill depends on an ARI API key and can export reports or reviews to local files.

Mitigation: Store credentials only through ARI_API_KEY or the local user configuration flow, avoid placing keys in reports or examples, and verify export destinations before creating local files.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [Amazon Bullet Optimization Operation Workflow](artifact/references/operation-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/bullet-writer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command snippets and ARI report links or JSON responses when commands are used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed listing/bullets workflow and requires an ARI API key; paid operations require explicit user confirmation.]

## Skill Version(s):

1.4.3 (source: evidence.json release.version, SKILL.md frontmatter, artifact/_meta.json, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
