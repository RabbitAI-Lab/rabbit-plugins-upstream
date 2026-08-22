## Description:

Analyzes aquarium camera images or videos to flag side-swimming, upside-down posture, axial rotation, floating or sinking behavior, and report abnormal-duration ratios for fish health monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarists, aquarium operators, ornamental fish farms, and smart-aquarium integrators use this skill to analyze fixed-camera fish-tank video or image inputs and review structured posture-health reports. The skill supports visual monitoring and suggested next actions, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos, video URLs, and history queries are sent to the publisher's cloud service.

Mitigation: Use only with consent for remote processing, disclose cloud submission before deployment, and avoid sending sensitive or unauthorized footage.

Risk: The skill can silently create or reuse a persistent internal identity and store tokens locally.

Mitigation: Require explicit opt-in for identity creation and history lookup, document token storage and database location, and provide a way to inspect, reset, or delete local identity state.

Risk: Visual posture analysis may be mistaken for a medical diagnosis or may misclassify species with naturally unusual swimming postures.

Mitigation: Present outputs as visual monitoring signals only, configure species-specific baselines and thresholds, and direct users to qualified aquarium or veterinary professionals for health decisions.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown text with structured JSON report content and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include abnormal posture classifications, observed duration metrics, abnormal-ratio summaries, history listings, and export links.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
