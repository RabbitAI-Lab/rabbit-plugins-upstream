## Description:

Analyzes aquarium camera images or videos for fish gasping, rapid mouth movement, and exaggerated gill movement, then produces a visual risk warning for possible hypoxia or ammonia-related water quality issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, public aquarium operators, aquaculture staff, and developers can use this skill to review fixed-camera footage for early visual warning signs of fish gasping or abnormal respiration. The output supports urgent water-quality checks, aeration, water-change planning, and escalation to aquatic specialists without presenting the result as a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos or URLs are sent to LifeEmergence remote services for analysis.

Mitigation: Use only media the user is authorized to submit, confirm consent before deployment, and document which remote endpoints receive video or URL data.

Risk: The skill may silently create or reuse an internal identity and store returned tokens in a local SQLite database.

Mitigation: Review token storage and deletion behavior before installation, restrict workspace access to the database, and provide clear user-facing consent and retention documentation.

Risk: A visual warning could be mistaken for a diagnosis of ammonia poisoning, nitrite poisoning, gill disease, or another specific condition.

Mitigation: Present outputs as visual risk warnings only, require immediate water-quality testing, and recommend confirmation by a qualified aquarium veterinarian or aquaculture technician.

Risk: Camera coverage, water-surface disturbance, floating plants, tracking failures, feeding behavior, or air-breathing fish species can make gasping detection unreliable.

Mitigation: Require suitable camera coverage and frame rate, apply species and feeding-context baselines, and return an unreliable-signal result when tracking quality or visibility is insufficient.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON reports with warning levels, observed fish behavior metrics, recommended actions, disclaimers, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save report output to a user-specified file; history queries return Markdown tables derived from the remote service.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata; artifact frontmatter is 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
