## Description:

Assesses legal AI systems against LGD registration, evidence, and review gates, returning scores and a gate decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and legal teams use this skill to review legal AI research, drafting, and opinion-assistance systems against an LGD checklist before relying on their outputs. Its scores and gate decision are advisory, not a legal opinion or certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested agent tool permissions exceed those needed for the local checklist.

Mitigation: Narrow permissions to reading inputs and running the local Python script before installation.

Risk: Checklist scores could be mistaken for legal advice or a certification.

Mitigation: Treat results as advisory and require qualified human review before legal decisions.

Risk: The source usage instructions include CLI flags that the script does not support.

Mitigation: Use the supported --rubric, --system, --answers, and --json flags instead.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-law-ethic)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scores by LGD law, a gate decision, and missing checklist items; the CLI also prints the rubric.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; source frontmatter states 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
