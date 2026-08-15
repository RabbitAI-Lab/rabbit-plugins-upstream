## Description:

Analyzes fixed-camera reptile enclosure video to estimate hourly movement, compare activity patterns with species circadian baselines, and produce a rhythm report with anomaly guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External keepers, breeders, researchers, and developers use this skill to process 24-hour or multi-day reptile enclosure videos, identify activity peaks and day/night rhythm alignment, and retrieve structured historical rhythm reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends enclosure videos or remote video URLs to lifeemergence.com services for analysis.

Mitigation: Review media content and deployment policy before use, especially when enclosure footage is sensitive or subject to retention limits.

Risk: The skill creates or reuses a persistent local identity and stores backend tokens or possible profile fields in workspace data.

Mitigation: Use an isolated workspace for deployments that require separate identities, and review local data storage before sharing or archiving the workspace.

Risk: The security verdict is suspicious because of cloud upload, history lookup, and local token persistence behavior.

Mitigation: Require operator review before installation and keep the skill's cloud API behavior visible in deployment documentation.

## Reference(s):

- [Reptile Circadian Activity Analysis API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-circadian-activity-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON analysis report with command-line usage and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include hourly activity arrays, peak and quiet hours, rhythm consistency scores, anomaly classification, recommendations, disclaimers, and report links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
