## Description:

Analyzes aquarium images or video to identify visual warning signs of fish gasping, fast respiration, and increased gill movement that may indicate hypoxia or ammonia-related risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, aquarium operators, and agent developers use this skill to analyze fixed aquarium camera media for visual warning signs of fish gasping and to produce risk-oriented reports and suggested next steps. It is suited to home aquariums, public aquariums, and aquaculture monitoring where outputs should be treated as visual risk warnings rather than medical or water-quality diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media and report history may be sent to a configured external service.

Mitigation: Review service configuration and obtain user approval before uploading media or querying history, especially for private homes, public aquarium facilities, or aquaculture operations.

Risk: The skill silently creates or reuses identity values and stores tokens in a local workspace SQLite database.

Mitigation: Document identity handling, restrict workspace access, and clear local token storage when the skill is no longer needed.

Risk: The published artifact includes private development HTTP endpoint configuration according to the authoritative security summary.

Mitigation: Use production HTTPS endpoints and validate endpoint settings before installation or operational use.

Risk: Visual analysis can produce misleading warnings when water surface visibility, fish tracking, or species baseline assumptions are unreliable.

Mitigation: Treat results as visual risk warnings only, verify water quality directly, and require human review before emergency interventions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured analysis report with risk level, observed indicators, suggested actions, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save results to a requested output file and may query historical reports through the configured service.]

## Skill Version(s):

1.0.13 (source: server release evidence; artifact SKILL.md frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
