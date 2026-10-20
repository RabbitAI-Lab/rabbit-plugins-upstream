## Description:

Provides an LGD three-law checklist and advisory gate assessment for privacy-computing and data-minimization scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers can assess a described AI system against LGD registration, evidence, and gate criteria before making privacy-computing deployment decisions. Results are advisory and require independent review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation claims automated privacy enforcement that the advisory checklist does not provide.

Mitigation: Review actual CLI behavior and supporting evidence; do not use its verdict alone to change access, publication, or service availability.

Risk: Requested agent tools include Write, WebFetch, and Bash beyond the checklist's needs.

Mitigation: Limit tool permissions to the minimum needed and require explicit approval for consequential actions.

Risk: Release license metadata conflicts with the documentation's code-only license and reserved rights for text.

Mitigation: Confirm licensing and scope with the publisher before reuse or redistribution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-crypto-guard)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rubric, per-law scores, gate verdict, and missing-evidence checklist; not an access-control mechanism.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; bundled skill documentation says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
