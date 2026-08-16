## Description:

This skill analyzes snake mouth images or videos to identify visible oral mucosa color changes, pus points, ulcers, necrotic tissue, image-quality issues, and context signals, then returns a stomatitis risk assessment with non-prescriptive care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as reptile keepers, breeding operations, and reptile veterinary teams use this skill to screen snake mouth imagery for visible signs associated with mouth rot risk and to produce structured reports. The output is a visual risk assessment and observation aid, not a veterinary diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends images, videos, and account-linked metadata to a configured remote service and may create or reuse an internal identity.

Mitigation: Use the skill only in deployments where cloud processing, local token storage, and account-linked history lookup are acceptable, and review configuration before installation.

Risk: The skill addresses animal health and may be mistaken for diagnosis or treatment advice.

Mitigation: Treat outputs as visual screening observations only; confirm suspected mouth rot or urgent findings with a qualified reptile veterinarian and avoid medication, dosage, or procedure recommendations.

Risk: Poor imagery, glare, incomplete mouth visibility, recent feeding, shedding, breeding injury, or unsuitable environmental context can cause unreliable assessment.

Mitigation: Require clear mouth-open imagery with adequate resolution and lighting, capture multiple frames where possible, collect species and husbandry context, and return an unreliable result when quality or context is insufficient.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-snake-stomatitis-detection-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON or Markdown report text, with optional saved file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk levels, visual observation fields, recommended non-prescriptive actions, report links, and history tables returned by the configured service.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
