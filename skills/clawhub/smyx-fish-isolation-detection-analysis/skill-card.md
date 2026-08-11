## Description:

This skill analyzes aquarium videos to track fish positions, compute the school centroid, and flag sustained isolation behavior when individuals remain beyond configured body-length distance thresholds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquaculture operators, and smart-camera developers use this skill to analyze continuous fish-tank or pond footage for schooling, isolation, centroid-distance, and alert-level reporting. It supports behavior monitoring and inspection workflows, not veterinary diagnosis or autonomous equipment control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos, video URLs, and history queries may be sent to lifeemergence.com services.

Mitigation: Use non-sensitive footage, confirm the destination service is acceptable, and avoid submitting private or regulated video content.

Risk: The skill may create or reuse an identity and store identity or session tokens in the local workspace.

Mitigation: Run it in a dedicated workspace or account and review or remove stored credentials after use.

Risk: Behavior alerts can be misleading when tracking quality is poor or species-specific baselines are not considered.

Mitigation: Treat outputs as monitoring guidance, require human review for interventions, and do not use the skill for veterinary diagnosis or autonomous equipment control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-isolation-detection-analysis)
- [Fish Isolation Detection API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown reports with structured JSON-capable analysis results, alert summaries, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save results to a user-specified output file and may query cloud-hosted history associated with the resolved identity.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
