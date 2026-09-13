## Description:

Analyzes fixed-camera video from kindergartens, early-education centers, or playgrounds to report children's social-interaction frequency, duration, initiators, interaction types, and heatmaps without providing psychological or autism diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External educators, childcare operators, and authorized agents use this skill to analyze classroom or playground video for social-interaction statistics, low-interaction candidates, and report links. It is intended as educational decision support and not as a medical or developmental diagnosis tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes videos of children and may expose sensitive minor-related footage or reports through remote processing and cloud report access.

Mitigation: Use only with documented guardian and institution consent, confirmed processor retention and deletion terms, encrypted storage, and access controls appropriate for childcare or school environments.

Risk: The security evidence flags silent identity creation and local bearer-token persistence.

Mitigation: Install only in an isolated workspace, use narrowly scoped credentials, avoid shared machines, and review or remove silent account creation and plaintext token storage before deployment.

Risk: The security evidence flags plaintext HTTP development endpoints in the package.

Mitigation: Configure HTTPS-only production endpoints and verify that no local or test HTTP endpoints are active before real use.

Risk: Social-interaction measurements could be misread as clinical or developmental diagnoses.

Mitigation: Present outputs as visual behavior statistics and directional attention prompts only; route developmental or autism concerns to qualified professionals.

## Reference(s):

- [Child Social Interaction Analysis API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-social-interaction-analysis-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown and JSON report text with report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured interaction counts, durations, initiator statistics, low-interaction candidates, social heatmap URLs, summaries, alerts, and historical report lists.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
