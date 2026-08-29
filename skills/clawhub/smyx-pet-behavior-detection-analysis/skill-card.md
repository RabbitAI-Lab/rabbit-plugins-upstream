## Description:

Identifies common abnormal pet behaviors such as scratching, biting, destructive chewing, jumping, digging, chasing, and separation anxiety, helping owners understand their pet's habits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze pet monitoring videos or video URLs, identify common abnormal pet behaviors, and return structured behavior reports, suggestions, and report links. It can also query cloud-stored historical behavior reports for the associated user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, video URLs, and identity-linked report data are sent to the provider for analysis and history lookup.

Mitigation: Install only when this data sharing is acceptable, and review the provider's privacy, retention, and access controls before use.

Risk: The skill silently creates or reuses an identity and stores account tokens for report association.

Mitigation: Review the automatic identity flow and local token storage behavior before deployment, especially on shared systems.

Risk: Cloud history lookup can expose prior reports associated with the resolved identity.

Mitigation: Verify that report history access is scoped to the intended user and that permissions match the deployment environment.

Risk: Default API configuration includes provider-hosted services and configurations that should be reviewed before use.

Mitigation: Confirm endpoint configuration and transport security before enabling the skill in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-behavior-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports, JSON analysis output, CLI command examples, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a file and may render historical report lists as Markdown tables.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
