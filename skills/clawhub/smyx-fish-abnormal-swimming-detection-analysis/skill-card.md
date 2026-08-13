## Description:

Analyzes aquarium videos or video URLs to identify abnormal fish swimming posture such as side-swimming, upside-down posture, axial rotation, floating, or sinking, and reports abnormal-duration ratios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, aquarium operators, and developers use this skill to analyze fixed-camera aquarium media for visual posture anomalies and generate structured monitoring results, report links, and suggested follow-up actions. It is intended to support observation and escalation, not to diagnose fish disease.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends aquarium media or video URLs to a configured external service for analysis.

Mitigation: Use only media that the user is authorized to submit, confirm the configured service endpoint is acceptable, and avoid submitting sensitive or unnecessary footage.

Risk: The skill may silently create or reuse an internal account identity and store service tokens locally.

Mitigation: Protect the workspace data directory, restrict access to stored state, and review or delete local account and token data when the skill is no longer used.

Risk: Visual posture results can be mistaken for a veterinary diagnosis.

Mitigation: Treat outputs as observation support only, configure species-specific baselines, and have significant or repeated abnormalities reviewed by a qualified aquarium professional or veterinarian.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Fish Abnormal Swimming API Documentation](artifact/references/api_doc.md)
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis output with report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an optional result file when an output path is provided.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
