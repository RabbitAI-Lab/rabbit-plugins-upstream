## Description:

Audits OpenClaw memory organization, redundancy, stale information, retrieval activity, and context overhead without modifying memory files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[broedkrummen](https://clawhub.ai/user/broedkrummen)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and administrators use this skill to review memory size and organization, identify possible redundancy or stale facts, and plan manual cleanup using cited evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit reads local memory and related bootstrap files, which may contain private information.

Mitigation: Run it only in a trusted workspace and keep report excerpts within the requested audience.

Risk: Heuristic matches and token estimates may lead to incorrect cleanup decisions.

Mitigation: Review cited lines and neighboring context, verify disputed facts, and apply any suggested edits manually.

## Reference(s):

- [ClawHub memory-audit release](https://clawhub.ai/broedkrummen/skills/memory-audit)
- [OpenClaw memory overview](https://docs.openclaw.ai/concepts/memory)
- [OpenClaw memory architecture](https://docs.openclaw.ai/concepts/memory-architecture)
- [OpenClaw dreaming](https://docs.openclaw.ai/concepts/dreaming)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Evidence-backed Markdown report; optional structured JSON from the analyzer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes file and line references, context-budget estimates, and recommendations for manual edits; does not change files.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
