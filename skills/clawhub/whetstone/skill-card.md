## Description:

Reviews software changes for failure risk, compatibility and sufficient verification. Use when a change affects shared data, public contracts, security, production or agent tool access, or when explicitly asked for Whetstone or a risk review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use Whetstone to review software changes for failure modes, compatibility concerns, and sufficient verification. It provides proportionate review guidance and an optional local diff scanner for security and change review cues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional diff scanner is heuristic, so its results may miss issues or flag harmless changes.

Mitigation: Treat scanner output as review cues rather than proof of safety; inspect relevant changes and run checks suited to the affected behavior. Use --staged or --no-untracked to limit the scan when appropriate.

## Reference(s):

- [Whetstone on ClawHub](https://clawhub.ai/ricardodpalmeida/skills/whetstone)
- [Security](references/security.md)
- [Verification](references/testing.md)
- [Contracts and failure handling](references/api-design.md)
- [Data changes](references/data-and-privacy.md)
- [Dependencies and build permissions](references/supply-chain.md)
- [Delivery and recovery](references/delivery-and-release.md)
- [AI boundaries](references/ai-features.md)
- [Accessibility](references/accessibility.md)
- [Stack checks](references/stack-checks.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with inline tables and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review guidance is tailored to the change's impact; scanner results are heuristic cues.]

## Skill Version(s):

0.2.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
