## Description:

Analyzes pet-camera images or videos for separation-anxiety behaviors, produces structured behavior reports, and recommends comfort interventions such as owner voice playback, treats, or interactive toys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, pet boarding centers, and developers use this skill to analyze pets left alone, identify possible separation-anxiety behaviors, review severity and timing, and receive non-diagnostic comfort recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-camera video, audio, or private video URLs may reveal sensitive home activity and are sent to the lifeemergence.com cloud service for analysis.

Mitigation: Use only media you are permitted to share, avoid highly sensitive recordings, and confirm that cloud handling meets the deployment's privacy and consent requirements before use.

Risk: The skill can create or reuse an internal identity, store authentication tokens locally, and retrieve cloud history without prompting every time.

Mitigation: Run it in an isolated workspace when possible, protect the workspace data directory, rotate or remove stored credentials after testing, and review history access expectations with users.

Risk: Behavior reports are observational and may be mistaken for veterinary or medical diagnosis.

Mitigation: Present results as behavioral guidance only and direct severe or persistent anxiety cases to a veterinarian or qualified pet behavior professional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-separation-anxiety-relief-analysis)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and JSON-style structured analysis, with optional saved output files and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files, video URLs, pet-type selection, detail-level selection, and cloud history listing.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
