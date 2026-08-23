## Description:

AI-powered pet vomiting and regurgitation detection from indoor fixed-camera video that reports observed event timing, frequency, motion cues, and vomitus characteristics for pet health monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet owners, animal-care teams, and agent operators use this skill to analyze fixed-camera pet footage for observed vomiting or regurgitation behavior, vomitus characteristics, event timing, and historical report lookup. Results are behavior observations and should not be treated as veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends indoor pet-camera footage and user-linked report history to the configured backend service.

Mitigation: Install only when the publisher and backend are trusted for this footage and history, and review data handling expectations before use.

Risk: The package can create or reuse a local identity and store service tokens for report access.

Mitigation: Run in an environment where local credential storage is acceptable, restrict filesystem access, and remove local state when the skill is no longer needed.

Risk: Configuration includes environment-specific endpoints and debug-oriented settings.

Mitigation: Review configuration before deployment and use production HTTPS endpoints appropriate for the runtime environment.

Risk: Visual analysis may miss events or confuse similar pet behaviors with vomiting or regurgitation.

Mitigation: Treat outputs as behavior observations, confirm important events with source footage or vomitus evidence, and seek veterinary review for concerning symptoms.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured report text, with optional saved file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observed event summaries, vomitus descriptions, risk prompts, report links, and historical report tables returned by the configured service.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
