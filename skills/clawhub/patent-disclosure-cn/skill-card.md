## Description:

Turns R&D materials, technical proposals, or early invention ideas into Chinese-language patent disclosure documents and review notes for an inventor and patent agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, researchers, and engineers use this skill to turn invention ideas or R&D documents into a patent technical disclosure and a separate checklist of assumptions and missing facts for review with a patent agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unfiled invention details and R&D materials are sent to a remote paid service with unclear upfront data-handling safeguards.

Mitigation: Confirm authorization to share the materials and review PatentMax's privacy and retention terms before submitting sensitive content.

Risk: An unexpected service endpoint could receive confidential invention materials.

Mitigation: Check that PATENTMAX_BASE_URL is not set to an unexpected host before use.

Risk: Trial credentials and task metadata are stored locally.

Mitigation: Protect access to ~/.patentmax and avoid exposing its contents.

Risk: Repeating a paid submission can incur another charge, while generated assumptions or patent comparisons may be mistaken for verified facts.

Mitigation: Get consent before paid submission, wait on the existing task rather than resubmitting, and have the inventor and patent agent review assumptions and novelty claims.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ip930/skills/patent-disclosure-cn)
- [Materials preparation guide](references/materials-guide.md)
- [Disclosure workflow](references/workflow.md)
- [Frequently asked questions](references/faq.md)
- [PatentMax service information](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [Chinese-language text and Word (.docx) documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a disclosure and separate review notes; can first suggest invention directions from a brief idea.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
